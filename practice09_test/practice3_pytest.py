import pytest
import practice2_unitest

is_release = True


class TestCal(object):
    @classmethod
    def setup_class(cls):
        cls.cal = practice2_unitest.Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        self.cal = practice2_unitest.Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        del self.cal

    def test_add_num_and_double(self):
        cal = practice2_unitest.Cal()
        assert cal.add_num_and_double(1, 1) == 4
        # assert로 판별 할 수 있다.
        # assertEqual 과 같은것을 기억 할 필요가 없다

    # @pytest.mark.skip(reason='skip!!')
    @pytest.mark.skipif(is_release == True, reason='skip!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            cal = practice2_unitest.Cal()
            cal.add_num_and_double('1', '1')
