import csv
import re

dataset = []

# read in the csv file and insert the impression column
with open(input("Enter input filename: "),"r") as input_file:
	dataset = list(csv.reader(input_file))
	header = True
	
	report_idx = None
	impression_idx = None

	# Scan header row to figure out what report index is
	for i, value in enumerate (dataset[0]):
		lowered = value.lower()
		if "report" in lowered:
			report_idx = i
			impression_idx = i+1
			break

	# Exit the program is no report column found
	if report_idx is None or impression_idx is None:
		exit("Couldn't find report column")

	# Searches the report text of every row and extracts the impression into the impression column
	for row in dataset:
		if header:	#the header row
			row.insert(impression_idx,"Impression")
			header = False
			continue
		report = row[report_idx]
		imp_match = re.search("IMPRESSION:.+",report,re.DOTALL)
		if imp_match is not None:
			row.insert(impression_idx,imp_match.group(0))
		else:
			row.insert(impression_idx,"No impression found")	

#write the dataset with impression inserted to designated file
with open(input("Enter output filename: "),"w") as output_file:
	csv.writer(output_file).writerows(dataset)