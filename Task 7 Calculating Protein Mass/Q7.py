import csv


def read_mass_table():
    with open("amino_acid_mass.csv", "r", newline='') as sgt:
        lines = csv.reader(sgt)
        table = []
        for l in lines:
            table.append(l)

    return table


with open("input.txt", "r") as file:
    s = file.readline()

# Raise error if string length is too long
if len(s) > 1000:
    ValueError("The string length is larger than the limit of 1000!")

# Print input text
print(f"Input protein string is: {s}")

# Read mass table
table = read_mass_table()

mass = 0

for char in s:
    for i in range(len(table)):
        if table[i][0] == char:
            mass += float(table[i][1])

print(f"The total weight of PP is: {round(mass, 5)}")