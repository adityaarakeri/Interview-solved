def is_armstrong(number):
    return sum(int(ch) ** len(str(number)) for ch in str(number)) == number
