from ops import mult, pow, add


def test_função_mult():
    assert mult(21, 2) == 42
    assert mult(5, 1) == 5
    assert mult(0, 2) == 0
    assert mult(-2, 3) == -6
    assert mult(2, 0) == 0


def test_função_add():
    assert add(21, 2) == 23
    assert add(5, 2) == 7
    assert add(0, 2) == 2
    assert add(-2, 3) == 1
    assert add(2, 0) == 2
    assert add(3, -2) == 1


def test_função_pow():
    assert pow(21, 2) == 21 * 21
    assert pow(5, 2) == 25
    assert pow(0, 2) == 0
    assert pow(-2, 3) == -8
    assert pow(2, 0) == 1
