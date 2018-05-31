import numpy as np

dataset = np.genfromtxt("data/names.csv",delimiter=",",dtype="U75")

print(dataset[:,:])

header = dataset[0,:]
dataset = dataset[1:,:]

name_idx = None

for i, each in enumerate(header):
	if "name" in each.lower():
		name_idx = i
		header[i] = "First Name"
		header.add(i+1,"Last Name")

for each in dataset:
	name_list = each[name_idx].split(" ")
	each[name_idx] = name_list[0]
	each[name_idx+1] = name_list[1]

print(header)

print(dataset[:10,:])