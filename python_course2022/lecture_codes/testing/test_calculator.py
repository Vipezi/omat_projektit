from calculator import *

def test_calculator():
    assert calculator("add", 1,1) == 2
    assert calculator("add", -1 ,1) == 0
    assert calculator("multiply", 2 ,3) == 6
    assert calculator("multiply", 10 ,0) == 0
    assert calculator("show", "kind" ,"mind") == ""