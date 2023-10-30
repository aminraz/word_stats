"""A Python Filter for analyzing text."""
import numpy as np
import sys

filename = sys.argv[1]
with open(filename, "r") as myfile:
    content = myfile.read()
    total_len = len(content)
    word_list = content.split()
    word_index = []  # index of a sentence beginning
    for index, word in enumerate(word_list):
        if word[-1] in (".", "!", "?"):
            word_index.append(index)
word_index = np.array(word_index)
sent_len = word_index[1:] - word_index[:-1]  # lenght of a sentence
sent_len = np.insert(sent_len, 0, word_index[0] + 1)
print(
    "The text has ",
    total_len,
    " characters, ",
    len(word_list),
    " words, and ",
    len(sent_len),
    " sentences.",
)
print(
    "The average lenght of a sentence is ",
    int(np.average(sent_len)),
    "word and standrd deviation of the length of sentence is {0:.1f}".format(
        np.std(sent_len)
    ),
    " word",
)

# creating a frequency table for words
punctuation = (".", ",", "!", "?")
identifiers = ("a", "an", "the")
for index, word in enumerate(word_list):
    if word[-1] in punctuation:
        word_list[index] = word[0:-1]
word_counts = {}  # creating a dictionary for words
for word in word_list:
    word_counts[word] = word_counts.get(word, 0) + 1

# calculating nomilized sum of frequency of words in a sentence.
sent_frq = []
for i in range(len(sent_len)):
    freq = 0
    if i == 0:
        for word in word_list[: word_index[i] + 1]:
            if word not in identifiers:
                freq = freq + word_counts.get(word)
        sent_frq.append(freq)
    else:
        for word in word_list[
            word_index[i - 1] + 1 : word_index[i] + 1
        ]:
            if word not in identifiers:
                freq = freq + word_counts.get(word)
        sent_frq.append(freq)

sent_frq = np.array(sent_frq)
sent_frq_nor = np.array(sent_frq / sent_len, dtype="float16")

# Type-Token Ratio (TTR)
TTR = len(word_counts) / len(word_list)
print("Type-Token Ratio (TTR): {0:.2f} ".format(TTR))
print(
    """
TTR measures the diversity or richness of vocabulary in a text.
TTR = (Number of unique word types) / (Total number of words)"""
)
# word_dict=word_counts.items()
# print("word_list: ", word_list)
# print("word_indxes: ", word_index)
# print("sent_frq: ", sent_frq)
# print("sent_frq_nor: {0}".format(sent_frq_nor))
