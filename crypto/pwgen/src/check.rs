fn main() -> std::io::Result<()>  {
    println!("What's the password?");
    let stdin = std::io::stdin();
    let mut line = String::new();
    stdin.read_line(&mut line)?;
    if line.trim() == include_str!("../password") {
        println!("{}", include_str!("../flag.txt"))
    } else {
        println!("Sorry, that isn't correct.");
    };
    Ok(())
}
