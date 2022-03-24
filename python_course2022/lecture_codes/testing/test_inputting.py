#! /usr/bin/python3

from inputting import *
import mock

def test_ask_from_user():
    with mock.patch('builtins.input', return_value = "yes"):
        assert ask_from_user() == True

    with mock.patch('builtins.input', return_value = "no"):
        assert ask_from_user() == False