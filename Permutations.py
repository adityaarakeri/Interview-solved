def permutations(lst):
  if len(lst) <= 1:
    return [lst]
  results = []
  for i in range(len(lst)):
    for perm in permutations(lst[:i] + lst[i+1:]):
      results.append([lst[i]] + perm)
  return results

# can also be done like this ;)
# import itertools
# def permutations(lst):
#
#     results=[]
#     for i in itertools.permutations(lst, len(lst)):
#         results.append(list(i))
#
#     return results

print permutations([1,2,3])

