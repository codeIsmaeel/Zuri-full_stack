# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content():
    with open('story.txt', 'r') as l:
        file = l.readlines()
        return file


# print(read_file_content())


def count_words():
    text = read_file_content("./story.txt")
    text_split = text.split()
    # create a dictionary to save the words and their count
    count = {}
    for word in text_split:
        if word in count:
            count[word] = + 1
        else:
            count[word] = 1
    return count


print(count_words())
