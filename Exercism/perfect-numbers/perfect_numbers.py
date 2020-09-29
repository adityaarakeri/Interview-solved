def classify(number):
    if number <= 0:
        raise ValueError("Bad number")
    sum_ = sum(i for i in range(1, number) if number % i == 0)
    if sum_ > number:
        return "abundant"
    elif sum_ < number:
        return "deficient"
    else:
        return "perfect"
