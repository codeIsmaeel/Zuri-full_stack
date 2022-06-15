# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


import string


# first attempt == wrong
# def read_file_content():
#     with open('story.txt', 'r') as l:
#         file = l.readlines()
#         return file


# print(read_file_content())


# def count_words():
#     text = read_file_content("./story.txt")
#     text_split = text.split()
#     # create a dictionary to save the words and their count
#     count = {}
#     for word in text_split:
#         if word in count:
#             count[word] = + 1
#         else:
#             count[word] = 1
#     return count


# print(count_words())


# second attempt:
# def read_file_content(filename):
#     with open("story.txt") as j:
#         reading = j.read()
#         return reading


# # print(read_file_content("story.txt"))


# def count_words():
#     file = read_file_content("story.txt")
#     txt_split = file.split()
#     print(txt_split)

#     word_count = {}
#     for word in txt_split:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     return word_count


# print(count_words())


# corrrected solution to task, the right thing should be:
# the mentor imported a function 'string'


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as l:
        file = l.read()
        return file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = text.translate(str.maketrans("", "", string.punctuation))
    text_split = text.split()
    # print("this is the text: \n", text)
    count = {}
    for word in text_split:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


print(string.punctuation)
print(count_words())
