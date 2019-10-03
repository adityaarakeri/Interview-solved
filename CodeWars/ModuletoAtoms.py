"""
For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map in Java).

For example:
water = 'H2O'
breakdown -> H2O1
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
breakdown -> Mg1O2H2
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
breakdown -> K4O2N2(SO3)4 -> K4O2N2S4O12
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}

"""

def parse_molecule(formula):

    word_stack = []
    num_stack = []
    formula = list(formula)
    brackets = {'}': '{', ']':'[', ')':'('}
    brackets1 = {'{': '}', '[':']', '(':')'}

    if not formula[-1].isdigit():
        formula.append('1')
    print(formula)

    

    # for i in range(len(formula) - 1):

    
    
print(parse_molecule('K4[ON(SO3)2]2'))



