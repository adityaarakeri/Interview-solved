from itertools import combinations, permutations

def get_value(v, mapper):
    return sum(mapper[b] * 10 ** (len(v) - i - 1) for i, b in enumerate(v))

def solve(puzzle):
    body, result = puzzle.split("==")
    result = result.strip()
    body = [i.strip() for i in body.split("+")]
    chars = list({ch for b in body for ch in b} | set(result))
    non_zero = set(n[0] for n in body + [result])
    mapper = {}

    for numbers in combinations(range(10), len(chars)):
        for c in permutations(chars):
            mapper = {c[i]: n for i, n in enumerate(numbers)}
            if any(mapper[n] == 0 for n in non_zero):
                continue
            lhs = sum(get_value(b, mapper) for b in body)
            rhs = get_value(result, mapper)
            if lhs == rhs:
                return mapper
    return {}
