def is_equal(a, b):
    if len(a) != len(b) or a[0] != b[0]:
        return False
    if len(a) == 1:
        return True
    return is_equal(a[1:], b[1:])


def test():
    assert is_equal(['a', 'm', 'o', 'r'], ['r', 'o', 'm', 'a']) == False
    assert is_equal(['a', 'm', 'o', 'r'], ['a', 'm', 'o', 'r', 'e']) == False
    assert is_equal(['a', 'm', 'o', 'r'], ['a', 'm', 'o', 'r']) == True
    print('Tests finished :)')


test()
