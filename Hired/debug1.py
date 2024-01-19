def solution(values, n , k) -> int:
    v1 = [x for x in values if x % k ==0]
    v1 = set(v1)
    v1 = sorted(v1, reverse=True)
    print(v1)
    count = 1
    for _ in v1:
        if count == k:
            return v1[count]
        count += 1

values = [4,9,3,12,6,4,15]
n = 4
k = 3
print(solution(values, n, k))