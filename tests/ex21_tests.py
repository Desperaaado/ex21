from nose.tools import *
from ex21.ex21 import *

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_bs_list():
    num = 55
    for i in range(0, 10):
        a_list = ordered_list()
        # print(a_list)
        # message = bs_list(num, a_list)
        # print(message)
        if num in a_list:
            result = num
        else:
            result = None
        assert bs_list(num, a_list) == result

def test_bs_dllist():
    num = 55
    for i in range(0, 10):
        a_dllist = ordered_dllist()
        a_dllist.dump()
        message = bs_dllist(num, a_dllist)
        a_dllist.dump()
        print(message)
        if num in a_dllist.dump('silence'):
            result = num
        else:
            result = None
        assert bs_dllist(num, a_dllist) == result