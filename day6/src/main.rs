use std::fs;

fn load_from_file(file_path: &str) -> Vec<i8>{
	let file_contents = fs::read_to_string(file_path).unwrap().replace('\n', "").replace('\r', "");
	let number_strings = file_contents.split(",").collect::<Vec<&str>>();
	println!("{:?}", number_strings);
	let numbers = number_strings.iter().map(|&nstr| nstr.parse::<i8>().unwrap()).collect::<Vec<i8>>();
	//println!("{:?}", numbers);
	//.parse().unwrap();

	return numbers;
}

fn simulate(ages: &mut Vec<i8>) {
	let mut new_fish_count = 0usize;
	for age in ages.iter_mut(){
		*age -= 1;
		if *age < 0 {
			*age = 6;
			new_fish_count += 1;
		}
	}
	let mut new_ages = vec![8; new_fish_count];
	ages.append(&mut new_ages);
}

fn main() {
	let mut ages = load_from_file("input");
	let days = 256;
	for day in 0..days {
		simulate(&mut ages);		
		println!("day {}: {} fish", day + 1, ages.len());
	}
}
