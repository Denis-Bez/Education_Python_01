def foo(a):
    result = [i if i % 2 else None for i in range(a)]
    return result

def test():
    assert foo(2) != [0, 1]

test()
# print(foo(-2))