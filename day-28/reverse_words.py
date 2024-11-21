"""
Reverse words in a sentence.
"""


def reverse_word(word: str) -> str:
    if not word:
        return " "
    chars = list(word)
    index = len(chars) - 1
    tmp = ""
    for i in range(len(chars)):
        tmp += chars[index]
        index -= 1
    return tmp


def reverse_sentence(sentence: str) -> str:
    reversed_sentence = ""
    for word in (sentence.split()):
        reversed_sentence += reverse_word(word) + " "
    return reversed_sentence


if __name__ == "__main__":
    my_sentence = "Hello World"
    print(reverse_sentence(my_sentence))
