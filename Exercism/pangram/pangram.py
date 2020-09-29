from string import ascii_lowercase


def is_pangram(sentence):
    chars = set(ch for ch in sentence.lower() if ch in ascii_lowercase)
    return len(chars) == len(set(ascii_lowercase))
