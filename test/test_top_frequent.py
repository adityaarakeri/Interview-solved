import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))
from LeetCode.top_k_frequent import Solution
 
def test_topk():
    s = Solution()
    assert s.topKFrequent([1,1,1,2,2,3],2) == [1,2]