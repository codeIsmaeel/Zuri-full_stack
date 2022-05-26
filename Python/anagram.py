def find_anagram(word, anagram):
    # [assignment] Add your code here

    word = input('enter word: ')
    anagram = input('enter anagram: ')

    return sorted(word) == sorted(anagram)


print(find_anagram('word', 'anagram'))
