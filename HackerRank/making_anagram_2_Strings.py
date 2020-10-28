"""
https://www.hackerrank.com/challenges/making-anagrams/problem
"""


def makingAnagrams(s1, s2):
    if s1 == s2:
        return 0
    else:
        all = set(s1+s2)
        k1 = {i: s1.count(i) for i in all}
        k2 = {i: s2.count(i) for i in all}
        k3 = {}
        for i, v in k1.items():
            diff = abs(k1[i]-k2[i])
            k3[i] = diff

        count = sum(k3.values())

        return count


if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)
    print(result)
