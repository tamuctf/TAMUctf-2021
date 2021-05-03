use nix::unistd::{setuid, Uid};
use pwd::Passwd;

fn main() {
    setuid(Uid::from_raw(
        Passwd::from_name("root").unwrap().unwrap().uid,
    ))
    .expect("Failed to set uid");

    println!("{}", std::fs::read_to_string("/root/flag").unwrap());
}
