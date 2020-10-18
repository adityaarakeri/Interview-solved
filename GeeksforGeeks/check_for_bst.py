"""
Given a binary tree. Check whether it is a BST or not.

Example 1:

Input:
    2
 /    \
1      3
Output: 1

Problem link :- 
https://practice.geeksforgeeks.org/problems/check-for-bst/1/?company[]=Amazon&problemStatus=solved&problemType=functional&page=1&sortBy=submissions&query=company[]AmazonproblemStatussolvedproblemTypefunctionalpage1sortBysubmissions

"""


INT_MAX = 4294967296
INT_MIN = -4294967296

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


def isBST(node):
    return checkBST(node,INT_MIN,INT_MAX)

def checkBST(node,mini,maxi):
    if node==None:
        return 1
    else:
        if node.data<=mini or node.data>=maxi:
            return 0
        else:
            return (checkBST(node.left,mini,node.data) and checkBST(node.right,node.data,maxi))
        
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        if isBST(root):
            print(1) 
        else:
            print(0)
