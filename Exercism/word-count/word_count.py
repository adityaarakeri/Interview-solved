from string import ascii_letters, punctuation


def clean(word):
    start, end = 0, len(word)
    while start < len(word) and word[start] in punctuation:
        start += 1
    while end >= 0 and word[end-1] in punctuation:
        end -= 1
    if end > start:
        return word[start:end]

def word_count(phrase):
    alternative_seps = [',', '_']
    for sep in alternative_seps:
        phrase = phrase.replace(sep, " ")
    words = [clean(word) for word in phrase.lower().split() if clean(word)]
    return {word:words.count(word) for word in set(words)}
