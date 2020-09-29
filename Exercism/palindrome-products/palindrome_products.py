def is_palindromic(number):
    return str(number) == "".join(reversed(str(number)))


def find_factors(number, min_factor, max_factor):
    factors = []
    for i in range(min_factor, max_factor+1):
        if number % i == 0 and max_factor >= number // i >= min_factor:
            factors.append((i, number // i))
    return number, factors


def largest_palindrome(max_factor, min_factor):
    all_numbers = set([])
    for i in range(max_factor, min_factor + 1, -1):
        for j in range(max_factor, min_factor + 1, -1):
            product = i * j
            if is_palindromic(product):
                all_numbers.add(product)
                break
        if len(all_numbers) > 100:
            break
    if not all_numbers:
        raise ValueError("No palindromic number found.")
    return find_factors(max(all_numbers), min_factor, max_factor)


def smallest_palindrome(max_factor, min_factor):
    all_numbers = set([])
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            product = i * j
            if is_palindromic(product):
                all_numbers.add(product)
                break
            if len(all_numbers) > 100:
                break
    if not all_numbers:
        raise ValueError("No palindromic number found.")
    return find_factors(min(all_numbers), min_factor, max_factor)
