"""
Write a function that receives string and number,
and returns original string if number <= length of string, or
string filled with spaces before original string with length = number

Example 
>> string_fill("abc", 7)
    abc
>> string_fill("abc", 2)
abc
"""

def string_fill(original_str: str, number: int) -> str:
    if len(original_str) >= number:
        return original_str
    else:
        count_spaces = number - len(original_str)
        return " " * count_spaces + original_str


#execute the function
string_fill("abc", 7)
