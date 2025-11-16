
def is_anagram(word1, word2):
    pass


def is_palindrome(word1: str):
    reversed_word = word1[::-1]
    return reversed_word == word1

def test_is_palindrome_true():
    assert is_palindrome('kayak')

def test_is_palindrome_false():
    assert not is_palindrome('tooth')




def is_pangram(word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters_in_word: set = set(word)
    # create for loop to check if set has all the letters

    print(len(letters_in_word))


is_pangram('claigragdffg')
    








