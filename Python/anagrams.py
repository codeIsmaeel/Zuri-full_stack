# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    word = input('enter word: ')
    anagram = input('enter anagram: ')

    sorted_word = sorted(word)
    sorted_anagram = sorted(anagram)

    if len(word) == len(anagram):
        if word.islower == anagram.islower:

            if sorted_word == sorted_anagram:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


print(find_anagram('word', 'anagram'))
