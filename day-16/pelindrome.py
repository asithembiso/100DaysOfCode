"""
Write a function to check if a given string is a palindrome.
"""


def is_palindrome(word: str) -> bool:
    if len(word) == 1:
        return True
    len_word = len(word) - 1
    tmp = ""
    while len_word >= 0:
        tmp += word[len_word]
        len_word -= 1
    return tmp == word


if __name__ == "__main__":
    print(is_palindrome("kayak"))
    print(is_palindrome("wow"))
    print(is_palindrome("rotator"))
    print(is_palindrome("mike"))
    print(is_palindrome("noon"))
