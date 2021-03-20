import pytest
import funcs


def check_getpath():
    assert funcs.get_path('test', 'test1') == 'test/test1'
    assert funcs.get_path(['test', 'test1']) == 'test/test1'
    assert funcs.get_path(['test']) == 'test'
    assert funcs.get_path('test') == 'test'
    try:
        funcs.get_path()
    except AttributeError:
        pass
    except:
        raise Exception('Returned invalid error')
