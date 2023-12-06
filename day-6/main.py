def find_characters_different(data):
    for i in range(len(data) - 4):
        if len(set(data[i:i + 4])) == 4:
            return i + 4


def tests():
    assert find_characters_different("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7, "Should be 7"
    assert find_characters_different("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5, "Should be 5"
    assert find_characters_different("nppdvjthqldpwncqszvftbrmjlhg") == 6, "Should be 6"
    assert find_characters_different("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10, "Should be 10"
    assert find_characters_different("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11, "Should be 11"


if __name__ == "__main__":
    tests()
    x = open('../inputs/day06.txt', 'r').read()
    print(find_characters_different(x))
