# test를 실행할때 이것부터 제일 먼저 본다
import pytest


@pytest.fixture
def csv_file():
    with open('test.csv', 'w+') as c:
        print('before test')
        yield c
        print('after test')


def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')
