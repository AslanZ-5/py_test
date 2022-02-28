import pytest

@pytest.fixture
def fixture_1():
    print('run_fixture.1')
    return 1

@pytest.mark.slow
def test_ex(fixture_1):
    num = fixture_1
    assert num == 1
def test_ex2():
    print('Helllowowdf')
    assert 1 == 1
def test_ex3():
    assert 1 == 1
def test_ex4():
    assert 1 == 1
def test_ex5():
    assert 1 == 1
