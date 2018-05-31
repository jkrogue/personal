import pandas as pd

data = pd.read_csv(input("Enter input filename: "))

columns = data.columns.tolist()

other_cols = []
name_col = None
for each in columns:
    if "first" in each.lower():
        exit("First name column already exists")
    if "name" in each.lower():
        name_col = each
    else:
        other_cols.append(each)
if name_col == None:
    exit("No name column found")
    
columns = ["First name", "Last name"] + other_cols
data["First name"] = data[name_col].apply(lambda x: x.split(" ")[0])
data["Last name"] = data[name_col].apply(lambda x: " ".join(x.split(" ")[1:]))

data = data[columns]

data.to_csv(input("Enter output filename: "), index=False)