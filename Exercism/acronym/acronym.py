def abbreviate(words):
    special_seps = ["-"]
    for sep in special_seps:
        words = words.replace(sep, ' ')
    return ''.join(word[0].upper() for word in words.split())
