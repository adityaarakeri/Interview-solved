Test cases for 7.py found in the LeetCode folder.
Answer by @VGZELDA
"""

# function to be tested
def reverse(self, x: int) -> int:
        x=int(x)
        if(x>=0):
            x=str(x)
            x=x[::-1]
            x=int(x)
            if(x<-1*(2**31))or(x>=2**31):
                return 0
            else:
                return x
        else:
            x=x*(-1)
            x=str(x)
            x=x[::-1]
            x=int(x)
            x=-1*x
            if(x<-1*(2147483648))or(x>=2147483648):
                return 0
            else:
                return x
# function to test reverse
def test_reverse():
    assert reverse(123) == 321, "Should be 321"
    assert reverse(120) == 21, "Should be 21"

if __name__ == "__main__":
    test_reverse()
    print("Everything passed")
