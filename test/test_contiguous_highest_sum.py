import Important.contiguous_highest_sum as m

def test_contigous_regular():
    assert m.contiguous_pair([5,2,4,6,3,1]) == [4,6]

def test_contigous_small():
    assert m.contiguous_pair([5,2]) == [5,2]

def test_contigous_empty():
    assert m.contiguous_pair([]) == []
