import os
import pytest
import practice1_doctest


# pytest 에 cov 는 얼마만큼 테스트가 진행되었는지에 대해 terminer 상으로 나타 내어 줌
class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = practice1_doctest.Cal()
        cls.test_dir = '/tmp/test_dir'
        cls.test_file_name = 'test.txt'

    @classmethod
    def teardown_class(cls):
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)  # test_dir을 클린 업 해주는 역할을 한다

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(
            self.test_dir, self.test_file_name
        )
        assert os.path.exists(test_file_path) is True

    # def test_add_num_and_double(self, request):  # request(객체)를 할경우 conftest로 받아옴
    #     os_name = request.config.getoption('--os-name')  # conftest에 option을 넣어주는 것
    #     if os_name == 'win':
    #         print('dir')
    #     elif os_name == 'mac':
    #         print('ls')
    #     assert self.cal.add_num_and_double(1, 1) == 4
    #
    # def test_add_num_and_double_next(self, tmpdir):
    #     print(tmpdir)
    #     assert self.cal.add_num_and_double(1, 1) == 4
    #
    # def test_save(self, tmpdir):  # arguemtn에 -s를 붙여줘야함
    #     self.cal.save(tmpdir, self.test_file_name)
    #     test_file_path = os.path.join(
    #         tmpdir, self.test_file_name)  # 2 file을 연결
    #     assert os.path.exists(test_file_path) is True

    def test_fixture_file(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
