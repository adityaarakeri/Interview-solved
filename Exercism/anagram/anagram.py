def detect_anagrams(word, candidates):
    valid = lambda x: sorted(x) == sorted(word.lower()) and x != word.lower()
    return [c for c in candidates if valid(c.lower())]
