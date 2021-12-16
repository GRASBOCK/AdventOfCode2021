use std::fs;

fn load_from_file(file_path: &str) -> Vec<usize>{
	let file_contents = fs::read_to_string(file_path).unwrap().replace('\n', "").replace('\r', "");
	let number_strings = file_contents.split(",").collect::<Vec<&str>>();
	println!("{:?}", number_strings);
	let ages = number_strings.iter().map(|&nstr| nstr.parse::<usize>().unwrap()).collect::<Vec<usize>>();
	//println!("{:?}", numbers);
	//.parse().unwrap();
	let &max_value = ages.iter().max().unwrap();
	let mut fish_by_age = vec![0 ; *vec![max_value, 8].iter().max().unwrap() + 1];
	for age in ages{
		fish_by_age[age] += 1;
	}
	println!("{:?}", fish_by_age);
	return fish_by_age;
}

fn simulate(fish_by_age: &Vec<usize>) -> Vec<usize> {
	let mut new_fish_by_age = fish_by_age.clone();
	let new_fish = fish_by_age[0];
	for i in 1..fish_by_age.len(){
		new_fish_by_age[i - 1] = new_fish_by_age[i]
	}
	new_fish_by_age[8] = new_fish; // new born fish
	new_fish_by_age[6] += new_fish; // fish who just now gave birth

	new_fish_by_age
}

fn main() {
	let mut fish_by_age = load_from_file("input");
	let days = 256;
	for day in 0..days {
		fish_by_age = simulate(&fish_by_age);
		println!("day {}: {} fish", day + 1, fish_by_age.iter().fold(0, |a, x| a + x));
	}
}
