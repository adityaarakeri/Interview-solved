from Company.vowel_count import count


def test_count():
    assert count('Alabama') == 4
    assert count('Caserta') == 3
