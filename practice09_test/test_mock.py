import unittest
from unittest.mock import MagicMock
from unittest import mock

import practice6_mock


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = practice6_mock.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        # 해당 코드를 실행 하고 나서 결과로 1을 반환 하돌고 하는 것
        self.assertEqual(s.calculation_salary(), 101)
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        # assert_called_once once를 더 붙이면 한번만 불러졌는지 판별
        # assert_called_with(year=2019) : yaer이라는 정보가 2019를 받아 지를 판별 해줌
        # assert_called_once_with 로 둘다 합친 코드로 작성할 수 있음
        # 해당 코드가 호출 되서 사용되었는지를 판별 해 주는역할을 한다

    def test_calculation_salary_no_salary(self):
        s = practice6_mock.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()

    @mock.patch('practice6_mock.ThirdPartyBonusRestApi.bonus_price',
                return_value=1)  # mock 를 path로 가져오는거
    def test_calculation_salary_path(self, mock_bonus):  # mock 로 인식
        # setting
        # mock_bonus.return_value=1 #위에 어노테이션 에 return value 를 안 넣어도됨

        # do
        s = practice6_mock.Salary(year=2017)
        salary_price = s.calculation_salary()

        # check
        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    # 위 코드와 동일
    def test_calculation_salary_path_with(self):  # mock 로 인식
        # setting
        with mock.patch('practice6_mock.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1  # 위에 어노테이션 에 return value 를 안 넣어도됨

            # do
            s = practice6_mock.Salary(year=2017)
            salary_price = s.calculation_salary()

            # check
            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    def setUp(self):
        self.patcher = mock.patch('practice6_mock.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()  # 이때 모크로 쓴다

    def tearDown(self):
        self.patcher.stop()

    # 위의 setUp 과 tearDown으로 하여도된다
    def test_calculation_salary_path_patcher(self):  # mock 로 인식
        # setting
        self.mock_bonus.return_value = 1  # 위에 어노테이션 에 return value 를 안 넣어도됨

        # do
        s = practice6_mock.Salary(year=2017)
        salary_price = s.calculation_salary()

        # check
        self.assertEqual(salary_price, 101)
        self.mock_bonus.assert_called()

    def test_calculation_salary_path_side_effect(self):  # mock 로 인식
        # setting
        def f(year):  # 해당내용으로 바꿔서 사용할 수 있다
            return year * 2

        self.mock_bonus.side_effect = f  # 위에 어노테이션 에 return value 를 안 넣어도됨
        # self.mock_bonus.side_effect = lambda year: 1
        # 복잡하지 않으면 lambda 를 하여도 된다

        # do
        s = practice6_mock.Salary(year=2017)
        salary_price = s.calculation_salary()

        # check
        self.assertEqual(salary_price, 4134)
        self.mock_bonus.assert_called()

    def test_calculation_salary_path_side_effect_error(self):  # mock 로 인식
        # setting
        # self.mock_bonus.side_effect = ConnectionRefusedError #error일 경우 처리해 줄수 있다
        self.mock_bonus.side_effect = [
            1, 2, 3, ValueError('Bankrupt!!!')
        ]
        # 복잡하지 않으면 lambda 를 하여도 된다
        # error일 경우를 check를 하는 것

        # do
        s = practice6_mock.Salary(year=2017)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 101)
        s = practice6_mock.Salary(year=2018)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 102)
        s = practice6_mock.Salary(year=2019)
        salary_price = s.calculation_salary()
        self.assertEqual(salary_price, 103)
        s = practice6_mock.Salary(year=200)
        with self.assertRaises(ValueError):
            s.calculation_salary()

    @mock.patch('practice6_mock.ThirdPartyBonusRestApi', spec=True)
    # spec 로 해당 class 의 모든 method 와 정보들을 전부 mock 할 수 있다
    def test_calculation_salary_class(self, MockRest):  # mock 로 인식
        # setting
        # mock_rest = MockRest.return_value # 이렇게 사용해도  밑에 꺼와 동일
        mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1  # 위에 어노테이션 에 return value 를 안 넣어도됨
        mock_rest.get_api_name.return_value = 'Money'  # 기존 클래스 모두 mock 가능

        # do
        s = practice6_mock.Salary(year=2017)
        salary_price = s.calculation_salary()

        # check
        self.assertEqual(salary_price, 101)
        mock_rest.bonus_price.assert_called()
