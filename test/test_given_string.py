assert balanced('abcedaiuschiasuhdiuaxxxshyydyyyiaushdiuash') == False
assert balanced('aaabbbcccdddeeefff') == True
assert balanced('aaapppppp') == False

assert balanced("xxxyyy") == True
assert balanced("yyyxxx") == True
assert balanced("xxxyyyy") == False
assert balanced("yyxyxxyxxyyyyxxxyxyx") == True
assert balanced("xyxxxxyyyxyxxyxxyy") == False
assert balanced("") == True
assert balanced("X") == True
