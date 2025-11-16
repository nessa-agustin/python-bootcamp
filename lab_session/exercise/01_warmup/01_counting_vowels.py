def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count

given_text = input('Enter string to count: ')
result = count_vowels(given_text)
print(f'{result} vowels counted for "{given_text}"')
