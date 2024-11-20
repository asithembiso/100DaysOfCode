"""
Find the longest word in a sentence.
"""


def longest_word(sentence: str) -> str:
    list_sentence = sentence.split(" ")
    if len(list_sentence) == 1:
        return sentence
    longest = ""
    for word in list_sentence:
        if len(longest) < len(word):
            longest = word
    return longest


if __name__ == "__main__":
    words = "I love Python"
    word2 = "I do not"

    print(longest_word(word2))
