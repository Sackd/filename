import sys
sys.path.append(".") 
import day0
import day1

def day0Test():
    res = day0.sum(1, 2)
    assert(res == 3)
    pass

def day1Test():
    res = day1.min(1, 2)
    assert(res == False)
    pass

day0Test()

day1Test()