"""
Write a function to count the number of vowels in a string.
"""


def find_vowels(string: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    # Remove spaces
    string = string.replace(" ", "").lower()
    for char in string:
        if char in vowels:
            counter += 1
    return counter


if __name__ == "__main__":
    word = "My name is Alex"
    print(find_vowels(word))
