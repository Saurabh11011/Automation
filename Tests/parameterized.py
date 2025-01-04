import pytest
import requests
import pdb

from urllib3 import request


@pytest.mark.parametrize("input,expected",[(1,2),(2,3),(3,5)])
def test_param(input,expected):
    # pdb.set_trace()
    assert input+1==expected,"what the heck is this "

def test_param2():
    a = [2,3,4,5,8]
    ls = (ev **2 for ev in a)
    print(list(ls))
    assert len(a) == 5

@pytest.mark.parametrize("expected",[(401,403,200)])
def test_add_one(expected):

    resp = requests.request()
    assert 401 in expected
