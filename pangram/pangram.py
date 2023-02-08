from string import ascii_lowercase

def is_pangram(sentence):
    letters = set(ascii_lowercase)
    sentence = sentence.lower()
    return letters <= set(sentence)
