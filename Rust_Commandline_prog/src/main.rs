//note that in Rust it is use and in C++ it is using.
use std::env;
use std::process;

mod lib;


fn main() {
    
    let args: Vec<String> = env::args().collect();
    let config = lib::Config::new(&args).unwrap_or_else(|err| { //unwrap_or_else aloows custom panic! errorr handling
    
    eprintln!("Problem parsing arguments: {}", err);
    process::exit(1);
        
        
    
});
    
    println!("Searching for {}", config.query);
    println!("In file {}", config.filename);
    
    if let Err(e) = lib::run(config) {
        eprintln!("Application error: {}", e);
        process::exit(1);
    }
}