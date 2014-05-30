from nose import with_setup

from fibonacci import fib

def setup_module(module):
    global c
    print "setting up the test"
    c = fib().calculate

def teardown_module(module):
    print "tearing everything down"

def test_number_0_1():
    assert c(0) == 0
    assert c(1) == 1
    
def test_number_5():
    assert c(5) == 5         
