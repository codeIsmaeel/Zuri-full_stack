# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


from fileinput import filename


def read_file_content(filename):
    with open('story.txt', 'r') as l:
        file = l.readlines()
        return file


def count_words(file):
    with open('story.txt', 'r') as j:
        single_word = j.split(' ')
        word_count = single_word.count
    # lib_count = word_count.__dict__
        return word_count


filename = ("story.txt")
read_file_content('story.txt')

count_words()
