test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

total_priority = 0
content = open('../inputs/day03.txt').read()

for item in content.splitlines():
    first_half = item[0:len(item) // 2]
    second_half = item[len(item) // 2:len(item)]
    print(first_half, second_half)

    matches = set(first_half) & set(second_half)
    print(matches)
    # items = set(first_half + second_half)
    priorities = [ord(item) - 96 if item.islower() else ord(item) - 38 for item in matches]
    print(priorities)
    total_priority += sum(priorities)


print(total_priority) # 7737

