from environ import Env

import param_store

from .utils import MockStore


def test_interpolate_dict():
    my_dict = {
        'TEST_VAR': 'ok',
        'TEST_DECRYPT': 'prefix-#{key-name}-data-#{missing}'
    }

    store = MockStore({
        'key-name': 'secret'
    })
    result = param_store.interpolate_dict(my_dict, store)

    assert result == {
        'TEST_VAR': 'ok',
        'TEST_DECRYPT': 'prefix-secret-data-#{missing}'
    }

