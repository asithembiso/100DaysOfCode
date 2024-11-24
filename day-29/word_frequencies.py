"""
Create a dictionary of words and their frequencies.
"""


def frequency(sentence: str):
    freq = {}
    sentence_array = sentence.split()
    for word in list(set(sentence_array)):
        count = 0
        for i in range(len(sentence_array)):
            if word == sentence_array[i]:
                count += 1
        freq[word] = count
    return freq


if __name__ == "__main__":
    words = "This is a sentence a is is a"
    print(frequency(words))

