# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors

# score:
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# + outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
ii = """A Y
B X
C Z
"""


def get_shape(word):
    switch = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    return switch.get(word, "Invalid value")


score = 0
content = open('../inputs/day02.txt', 'r').read()
for row in content.splitlines():
    first_col, second_col = row.split()[0], row.split()[1]
    shape = get_shape(second_col)

    if first_col == 'A' and second_col == 'Y':
        score += 6 + shape
    if first_col == 'A' and second_col == 'Z':
        score += 0 + shape
    if first_col == 'A' and second_col == 'X':
        score += 3 + shape

    if first_col == 'B' and second_col == 'X':
        score += 0 + shape
    if first_col == 'B' and second_col == 'Y':
        score += 3 + shape
    if first_col == 'B' and second_col == 'Z':
        score += 6 + shape

    if first_col == 'C' and second_col == 'X':
        score += 6 + shape
    if first_col == 'C' and second_col == 'Y':
        score += 0 + shape
    if first_col == 'C' and second_col == 'Z':
        score += 3 + shape

print(score) # 11603
