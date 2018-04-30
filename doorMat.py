# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Input Format

# A single line containing the space separated values of  and .

# Constraints



# Output Format

# Output the design pattern.

# Sample Input

# 9 27
# Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

try:
    N = int(raw_input("Enter the No of rows you need in your Mat: \n").strip()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
except: 
    print "Did not enter a number for the number of rows"

#no of coulmns calculated using N
M = N*3
for i in xrange(1,N,2): 
    print "{:-^{fill}}".format(".|." * i, fill=M)
print "{:-^{fill}}".format("WELCOME", fill=M)
for i in xrange(N-2,-1,-2): 
    print "{:-^{fill}}".format(".|."*i, fill=M)