class Allergies(object):
    SOURCES = [
        'eggs', 'peanuts', 'shellfish', 'strawberries',
        'tomatoes', 'chocolate', 'pollen', 'cats',
    ]

    def __init__(self, score):
        self.score = score % 256

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        return [self.SOURCES[i] for i, ch in enumerate(reversed(str(bin(self.score))[2:])) if ch == '1']
