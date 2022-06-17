'''

Excercise 7a

Building on the previous exercise, handle capitalized words—If a word is capitalized (i.e., the first letter is capital-
ized, but the rest of the word isn’t), then the Ubbi Dubbi translation should be
similarly capitalized.

'''

def ubbi_dubbi(word):
    output = []
    capitalized = False
    if word[0].isupper() and word[1].islower():
        capitalized = True
    for letter in word:
        if letter.lower() in 'aeiou':
            output.append('ub')
        output.append(letter)
    output = ''.join(output)
    if not capitalized:
        return output
    return f'{output[0].upper()}{output[1:].lower()}' # Capitalize first letter
    
print(ubbi_dubbi('Elephant'))
print(ubbi_dubbi('octopus')) 