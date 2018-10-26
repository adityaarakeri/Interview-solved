"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

"abcabcbb" ->"abc" -> 3
"bbbbb" ->"b" -> 1
"pwwkew" ->"wke" ->3
"pwke" is a subsequence and not a substring.

"""

# solution has a time complexity of O(n^2)
def longest_substring_without_repeat_brute(string):
	maximum_length = 0
	for i in range(len(string)):
		maximum_length = max(maximum_length, helper(string, i))
	return maximum_length

def helper(string, start):
	seen = set()
	for i in range(start, len(string)):
		if string[i] not in seen:
			seen.add(string[i])
		else:
			return i - start
	return len(string) - start

# sliding window solution
# time complexity is O(n)
def longest_substring_without_repeat(string):
	seen = {}
	maximum_length = 0
	start = 0
	for end in range(len(string)):
		if string[end] in seen:
			start = max(start, seen[string[end]] + 1)
		seen[string[end]] = end
		maximum_length = max(maximum_length, end - start + 1)
	return maximum_length

print(longest_substring_without_repeat_brute("abcabcbb") == 3)
print(longest_substring_without_repeat_brute("bbbbb") == 1)
print(longest_substring_without_repeat_brute("pwwkew") == 3)

print(longest_substring_without_repeat("abcabcbb") == 3)
print(longest_substring_without_repeat("bbbbb") == 1)
print(longest_substring_without_repeat("pwwkew") == 3)