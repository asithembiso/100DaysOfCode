"""
Write a function to convert a list of words into a sentence.
"""
from typing import List


def make_sentence(list: List) -> str:
    sentence = ""
    for word in list:
        sentence += word + " "
    return sentence


if __name__ == "__main__":
    words = ["I","am", "a", "sentence."]
    print(make_sentence(words))


