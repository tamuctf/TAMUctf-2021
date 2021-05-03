use reqwest::header::CONTENT_TYPE;
use std::convert::Infallible;
use warp::filters::path::FullPath;
use warp::Filter;

async fn request_screenshot(path: FullPath) -> Result<warp::http::Response<Vec<u8>>, Infallible> {
    // make sure this is actually base64 right quick
    match base64::decode(
        &path
            .as_str()
            .chars()
            .skip(1)
            .map(|c| c as u8)
            .collect::<Vec<u8>>(),
    ) {
        Ok(decoded) => match String::from_utf8(decoded) {
            Ok(_) => {
                let resp = reqwest::get(&("http://capture:9000".to_string() + path.as_str()))
                    .await
                    .unwrap();
                if resp.status() == 200 {
                    return Ok(warp::http::Response::builder()
                        .header(CONTENT_TYPE, "image/png")
                        .body(resp.bytes().await.unwrap().to_vec())
                        .unwrap());
                }
            }
            Err(_) => {}
        },
        Err(_) => {}
    }
    Ok(warp::http::Response::builder()
        .status(500)
        .body(Vec::new())
        .unwrap()) // nope
}

#[tokio::main]
async fn main() {
    let index = warp::path::end()
        .map(|| warp::reply::html(String::from_utf8_lossy(include_bytes!("index.html"))));
    let render = warp::path::full().and_then(request_screenshot);

    warp::serve(index.or(render))
        .run(([0, 0, 0, 0], 8000))
        .await;
}
