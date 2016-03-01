fn main() {
	let mut counter = 0;
	let mut a = 1;
	let mut b = 1;
	while a < 4000000 {
		let tmp = b;
        b += a;
        a = tmp;
        if a%2==0 {
            counter += a;
        }
	}
    println!("{}", counter);
}
