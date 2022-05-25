
# file = open('filee.txt', 'r')
# read_file = file.read()
# file_words = read_file.split(' ')
# print('Total Words: ', len(file_words))

# using user input to read text
text = input('Enter Desired Text: ')
# this line is not needed not needed: read_text = text.read()
text_words = text.split(' ')
print('Total words: ', len(text_words))
