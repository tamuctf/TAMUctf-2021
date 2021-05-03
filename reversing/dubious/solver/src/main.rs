use regex::Regex;
use std::fs::File;
use std::io::{BufReader, Read};
use std::ops::Add;
use std::str::FromStr;
use z3::ast::{Ast, Int, BV};
use z3::{Config, Context};
use z3::{SatResult, Solver};

fn main() {
    let file = File::open("check_flag.dump").expect("Couldn't find check_flag.dump");
    let mut dump = String::new();
    BufReader::new(file)
        .read_to_string(&mut dump)
        .expect("Couldn't read whole dump");

    let check_parse =
        Regex::new(r"[0-9a-f]+ <check_[0-9]+>:\n((?: {4}[0-9a-f]+:\t[0-9a-f]+ \t.+\n)+)").unwrap();
    let diff1_parse = Regex::new(r"[0-9a-f]+ <check_[0-9]+>:\n.*move\.4 -8\(sp\)\+\+,a6\n.*lea\.1 a6,4\(sp\)\n.*move\.4 \(a6\),d0\n.*move\.4 d0,\(a6\)\n.*add\.4 d0,#([0-9]+),d0\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*move\.1 d1,d0\n.*move\.4 d0,\(a6\)\n.*add\.4 d0,#([0-9]+),d0\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*move\.1 d0,d0\n.*add\.4 d0,#([0-9]+),d0\n.*sub\.4 d0,d1,d0\n.*sub\.4 d1,#0,d0\n.*addc d0,d0,d1\n.*move\.4 a6,\(sp\)8\+\+\n.*calli a5,0\(a5\)").unwrap();
    let diff2_parse = Regex::new(r"[0-9a-f]+ <check_[0-9]+>:\n.*move\.4 -8\(sp\)\+\+,a6\n.*lea\.1 a6,4\(sp\)\n.*move\.4 \(a6\),d0\n.*move\.4 d0,\(a6\)\n.*add\.4 d0,#([0-9]+),d0\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*move\.1 d1,d0\n.*move\.4 d0,\(a6\)\n.*add\.4 d0,#([0-9]+),d0\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*move\.1 d0,d0\n.*movei d2,#([0-9]+)\n.*add\.4 d0,d0,d2\n.*sub\.4 d0,d1,d0\n.*sub\.4 d1,#0,d0\n.*addc d0,d0,d1\n.*move\.4 a6,\(sp\)8\+\+\n.*calli a5,0\(a5\)").unwrap();
    let zdiff1_parse = Regex::new(r"[0-9a-f]+ <check_[0-9]+>:\n.*move\.4 -8\(sp\)\+\+,a6\n.*lea\.1 a6,4\(sp\)\n.*move\.4 \(a6\),d0\n.*move\.4 d0,\(a6\)\n.*add\.4 d0,#([0-9]+),d0\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*move\.1 d1,d0\n.*move\.4 d0,\(a6\)\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*move\.1 d0,d0\n.*movei d2,#([0-9]+)\n.*add\.4 d0,d0,d2\n.*sub\.4 d0,d1,d0\n.*sub\.4 d1,#0,d0\n.*addc d0,d0,d1\n.*move\.4 a6,\(sp\)8\+\+\n.*calli a5,0\(a5\)").unwrap();
    let zdiff2_parse = Regex::new(r"[0-9a-f]+ <check_[0-9]+>:\n.*move\.4 -8\(sp\)\+\+,a6\n.*lea\.1 a6,4\(sp\)\n.*move\.4 \(a6\),d0\n.*move\.4 d0,\(a6\)\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*move\.1 d1,d0\n.*move\.4 d0,\(a6\)\n.*add\.4 d0,#([0-9]+),d0\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*move\.1 d0,d0\n.*add\.4 d0,#([0-9]+),d0\n.*sub\.4 d0,d1,d0\n.*sub\.4 d1,#0,d0\n.*addc d0,d0,d1\n.*move\.4 a6,\(sp\)8\+\+\n.*calli a5,0\(a5\)").unwrap();
    let zdiff3_parse = Regex::new(r"[0-9a-f]+ <check_24>:\n.*move\.4 -8\(sp\)\+\+,a6\n.*lea\.1 a6,4\(sp\)\n.*move\.4 \(a6\),d0\n.*move\.4 d0,\(a6\)\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*move\.1 d1,d0\n.*move\.4 d0,\(a6\)\n.*add\.4 d0,#([0-9]+),d0\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*move\.1 d0,d0\n.*movei d2,#([0-9]+)\n.*add\.4 d0,d0,d2\n.*sub\.4 d0,d1,d0\n.*sub\.4 d1,#0,d0\n.*addc d0,d0,d1\n.*move\.4 a6,\(sp\)8\+\+\n.*calli a5,0\(a5\)").unwrap();
    let eq_parse = Regex::new(r"[0-9a-f]+ <check_[0-9]+>:\n.*move\.4 -8\(sp\)\+\+,a6\n.*lea\.1 a6,4\(sp\)\n.*move\.4 \(a6\),d0\n.*move\.4 d0,\(a6\)\n.*add\.4 d0,#([0-9]+),d0\n.*movea a3,d0\n.*move\.1 d1,\(a3\)\n.*move\.4 d0,\(a6\)\n.*add\.4 d0,#([0-9]+),d0\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*xor\.4 d0,d1,d0\n.*move\.1 d0,d0\n.*add\.4 d0,#-1,d0\n.*lsr\.4 d0,d0,#0x1f\n.*move\.4 a6,\(sp\)8\+\+\n.*calli a5,0\(a5\)").unwrap();
    let eqimm_parse = Regex::new(r"[0-9a-f]+ <check_[0-9a-f]+>:\n.*move\.4 -8\(sp\)\+\+,a6\n.*lea\.1 a6,4\(sp\)\n.*move\.4 \(a6\),d0\n.*move\.4 d0,\(a6\)\n.*add\.4 d0,#([0-9]+),d0\n.*movea a3,d0\n.*move\.1 d0,\(a3\)\n.*xor\.4 d0,#([0-9]+),d0\n.*move\.1 d0,d0\n.*add\.4 d0,#-1,d0\n.*lsr\.4 d0,d0,#0x1f\n.*move\.4 a6,\(sp\)8\+\+\n.*calli a5,0\(a5\)").unwrap();

    let config = Config::new();
    let ctx = Context::new(&config);
    let solver = Solver::new(&ctx);
    for (func, capture) in (0..).zip(check_parse.captures_iter(&dump)) {
        let check = capture.iter().next().unwrap().unwrap().as_str();
        if let Some(extracted) = diff1_parse
            .captures_iter(check)
            .next()
            .or_else(|| diff2_parse.captures_iter(check).next())
        {
            let mut args = extracted.iter().skip(1);
            let cmp1 = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            let cmp2 = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            let offset = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            println!("{} => p[{}] == {} + p[{}]", func, cmp1, offset, cmp2);
            let cmp1 = BV::new_const(&ctx, format!("p[{}]", cmp1), 8);
            let cmp2 = BV::new_const(&ctx, format!("p[{}]", cmp2), 8);
            let offset = BV::from_int(&Int::from_u64(&ctx, offset as u64), 8);
            solver.assert(&cmp1._eq(&offset.add(&cmp2)));
        } else if let Some(extracted) = zdiff1_parse.captures_iter(check).next() {
            let mut args = extracted.iter().skip(1);
            let cmp1 = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            let offset = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            println!("{} => p[{}] == {} + p[0]", func, cmp1, offset);
            let cmp1 = BV::new_const(&ctx, format!("p[{}]", cmp1), 8);
            let cmp2 = BV::new_const(&ctx, format!("p[{}]", 0), 8);
            let offset = BV::from_int(&Int::from_u64(&ctx, offset as u64), 8);
            solver.assert(&cmp1._eq(&offset.add(&cmp2)));
        } else if let Some(extracted) = zdiff2_parse
            .captures_iter(check)
            .next()
            .or_else(|| zdiff3_parse.captures_iter(check).next())
        {
            let mut args = extracted.iter().skip(1);
            let cmp2 = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            let offset = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            println!("{} => p[0] == {} + p[{}]", func, offset, cmp2);
            let cmp1 = BV::new_const(&ctx, format!("p[{}]", 0), 8);
            let cmp2 = BV::new_const(&ctx, format!("p[{}]", cmp2), 8);
            let offset = BV::from_int(&Int::from_u64(&ctx, offset as u64), 8);
            solver.assert(&cmp1._eq(&offset.add(&cmp2)));
        } else if let Some(extracted) = eq_parse.captures_iter(check).next() {
            let mut args = extracted.iter().skip(1);
            let cmp1 = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            let cmp2 = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            println!("{} => p[{}] == p[{}]", func, cmp1, cmp2);
            let cmp1 = BV::new_const(&ctx, format!("p[{}]", cmp1), 8);
            let cmp2 = BV::new_const(&ctx, format!("p[{}]", cmp2), 8);
            solver.assert(&cmp1._eq(&cmp2));
        } else if let Some(extracted) = eqimm_parse.captures_iter(check).next() {
            let mut args = extracted.iter().skip(1);
            let cmp = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            let value = u8::from_str(args.next().unwrap().unwrap().as_str()).unwrap();
            println!("{} => {} == p[{}]", func, value, cmp);
            let cmp = BV::new_const(&ctx, format!("p[{}]", cmp), 8);
            let value = BV::from_int(&Int::from_u64(&ctx, value as u64), 8);
            solver.assert(&cmp._eq(&value));
        } else {
            println!("No match found for {}", func);
        }
    }
    let mut pass = String::new();
    match solver.check() {
        SatResult::Sat => {
            let model = solver.get_model().unwrap();
            for i in 0..64 {
                let c = model
                    .eval(&BV::new_const(&ctx, format!("p[{}]", i), 8))
                    .unwrap()
                    .as_u64()
                    .unwrap() as u8 as char;
                pass.push(c);
            }
        }
        _ => {
            eprintln!("Solver status was not SAT.");
            return;
        }
    }
    println!("Password discovered: {}", pass);
}
