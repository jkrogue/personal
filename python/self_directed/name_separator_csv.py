import csv

dataset = []

# reads in a csv file, finds the name column automatically and separates it into first and last name columns
with open(input("Enter input filename: "),"r") as input_file:
	dataset = list(csv.reader(input_file))

	name_idx = None

	# find the name column
	for i, value in enumerate(dataset[0]):
		lowered = value.lower()

		# exit if the list already has separated first and last name columns
		if "name" in lowered and "first" in lowered:
			exit("list already separated into first and last names")

		elif "name" in lowered and "first" not in lowered:
			name_idx = i
			break

	# exit if no name column was found
	if name_idx == None:
		exit("couldn't find the name column")

	# go through each row, separate name into first and last by " ", and change original name column to first and inset last
	header = True
	for row in dataset:
		if header:
			row[name_idx] = "First Name"
			row.insert(name_idx+1,"Last Name")
			header = False
			continue
		name_list = row[name_idx].split(" ",1)
		row[name_idx] = name_list[0]	# add first name
		row.insert(name_idx+1,name_list[1:])	# add last name


# writes the dataset to the file
with open(input("Enter output filename: "),"w") as output_file:
	csv.writer(output_file).writerows(dataset)