use std::convert::Infallible;
use std::io::Read;
use warp::filters::path::FullPath;
use warp::Filter;

async fn request_screenshot(path: FullPath) -> Result<Vec<u8>, Infallible> {
    let dir = tempfile::tempdir().unwrap();

    let cmd = tokio::process::Command::new("google-chrome")
        .arg("--no-sandbox")
        .arg("--screenshot")
        .arg("--headless")
        .arg(
            "http://localhost:9000/chrome_gigem%7BlmA0_N1c3_10c4t1oN_buddy%7D".to_string()
                + path.as_str(),
        )
        .current_dir(dir.path())
        .spawn()
        .expect("Process failed to spawn. Dying fast.");

    assert!(cmd.await.expect("Child did not die?").success());

    let path = dir.path().join("screenshot.png");
    println!("{}", path.as_os_str().to_str().unwrap());

    Ok(std::fs::File::open(path)
        .map(|mut file| {
            let mut data = Vec::new();
            if file.read_to_end(&mut data).is_err() {
                Vec::new()
            } else {
                data
            }
        })
        .unwrap_or(Vec::new()))
}

#[tokio::main]
async fn main() {
    let chrome_available = warp::path!("chrome_gigem%7BlmA0_N1c3_10c4t1oN_buddy%7D" / String)
        .map(|b64: String| {
            println!("{}", b64);
            let decoded = base64::decode(&b64).unwrap();
            String::from_utf8(decoded).unwrap()
        })
        .map(|html| warp::reply::html(html));
    let render = warp::path::full().and_then(request_screenshot);

    warp::serve(chrome_available.or(render))
        .run(([0, 0, 0, 0], 9000))
        .await;
}
