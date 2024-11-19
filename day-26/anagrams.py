"""
Write a function check if two strings are anagrams.
"""


def anagram(str1: str, str2: str) -> bool:
    if str1 == str2:
        return True
    len_chars = 0
    list_str1 = list(str1.replace(" ", "").lower())
    list_str2 = list(str2.replace(" ", "").lower())

    for char in list_str1:
        if char in list_str2:
            len_chars += 1
        else:
            len_chars -= 1

    if len_chars == len(list_str2):
        return True
    return False


if __name__ == "__main__":
    word1 = "I am Lord Voldemort"
    word2 = "Tom Marvolo Riddle"
    print(anagram(word1, word2))
