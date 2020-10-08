# Function rotating the string
def rotate(s):
    return "".join([s[1:], s[0]])


def sa_char(bwt, c):
    """
    Function computing the SA range of a single character
    :param bwt: The BWT string
    :param c: input character
    :return: The range indices of SA
    """
    start = bwt.find(c)
    for i in range(start, len(bwt)):
        if bwt[i] != c:
            end = i - 1
            return start, end


def n_smaller_characters(bwt, c):
    """
    Function computing the number of characters smaller than c in BWT
    :param bwt: The BWT string
    :param c: input character
    :return: The number of characters smaller than c in BWT
    """
    count = 0
    for char in bwt:
        if char < c:
            count += 1

    return count


def sa_pattern(bwt, p):
    """
    Function computing the SA range of a single pattern
    :param bwt: The BWT string
    :param p: input pattern string
    :return: The SA range of the pattern
    """

    # Initial SA range
    u, v = sa_char(bwt, p[-1])

    # Iterate through the pattern string to update SA
    index = -1
    while True:
        u = n_smaller_characters(bwt, p[index]) + bwt[:u].count(p[index]) + 1
        v = n_smaller_characters(bwt, p[index]) + bwt[:v+1].count(p[index])

        if index == - len(p):
            return u, v

        index -= 1

# Read input file
with open("input.txt", "r") as file:
    s = file.readline()

# Append $
s = s + '$'
transform_matrix = []

# Create transform matrix
for _ in range(len(s)):
    transform_matrix.append(s)
    s = rotate(s)

# Sort the transform matrix and obtain suffix array
sa = sorted(range(len(transform_matrix)), key=lambda k: transform_matrix[k])
transform_matrix = sorted(transform_matrix)

# Obtain BWT
bwt = "".join([transform_matrix[i][-1] for i in range(len(s))])

# Find the SA range indices of a specific pattern
pattern = "eon"
u, v = sa_pattern(bwt, pattern)

print(f"The SA range found is: ({u}, {v})")
print(f"The positions found for pattern \"{pattern}\" is {sa[u:v+1]}")
