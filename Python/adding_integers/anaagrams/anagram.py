# def find_anagram(word, anagram):
#     # [assignment] Add your code here

#     word = input('enter word: ')
#     anagram = input('enter anagram: ')

#     return sorted(word) == sorted(anagram)


# print(find_anagram('word', 'anagram'))


#  corrected solution to finding anagrams task

def find_anagram(word, anagram):

    word = input("Enter word: ")
    anagram = input("Enter anagram: ")

    word = word.lower() .replace(" ", "") .strip()
    anagram = anagram.lower() .replace(" ", "") .strip()

    return sorted(word) == sorted(anagram)


print(find_anagram("word", "anagram"))
