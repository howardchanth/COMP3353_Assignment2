with open("input.txt", "r") as file:
    s = file.readline()
    t = file.readline()

count = 0

for m, n in zip(range(len(s)), range(len(t))):
    if s[m].upper() != t[n].upper():
        count += 1


print(f"The Hamming distance is: {count}")
