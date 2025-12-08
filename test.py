from main import simple_func


def test_simple_func():
    r1 = simple_func(1)
    r2 = simple_func(2)

    assert r1 == 2
    assert r2 == 1
