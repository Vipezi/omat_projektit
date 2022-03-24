from while_true import *
import mock

# Works
def test_ask_number():
    with mock.patch('builtins.input', side_effect = ["1", "one", "something"]):
        assert ask_number() == 1


'''
# Not working
with mock.patch('builtins.input', return_Value = "1"):
    assert ask_number() == 1
'''