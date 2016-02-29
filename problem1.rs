fn main() {
	let mut counter: i32 = 0;
	for n in 1..1000 {
		if (n%3 == 0) || (n%5 == 0) {
			counter = counter + n;
		}
	}
	println!("{}", counter);
}
