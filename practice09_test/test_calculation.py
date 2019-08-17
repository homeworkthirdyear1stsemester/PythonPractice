import unittest

import practice2_unitest

release_name = 'lesson'


# java의 test 랑 동일 하다
class CalTest(unittest.TestCase):
    def setUp(self):  # 각 테스트 실행 전 제일 먼저 실행
        print('setUp')
        self.cal = practice2_unitest.Cal()

    def tearDown(self):  # 각 테스트 실행 이후 마지막에 실행
        print('clean Up')
        del self.cal

    # @unittest.skip('skip!')  # 실행 시 이것은 무시하고 다른 거만 실행함
    @unittest.skipIf(release_name == 'lesson', 'skip!!')  # 만약 조건에 맞으면 skip함
    def test_add_num_and_double(self):
        cal = practice2_unitest.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 4)
        """
        assertEqual(a, b) a==b
        assertNotEqual(a, b) a != b
        assertTrue(x) bool(x) is True
        assertFalse(x) bool(x) is False
        assertIs(a, b) a is b 3.1
        assertIsNot(a, b) a is not b
        assertIsNone(x) x is None
        assertIsNotNone(x) x is not None
        assertIn(a, b) a in b
        assertNotIn(a, b) a not in b
        assertIsInstance(a, b) isinstance(a, b)
        assertNotIsInstance(a, b) not isinstance(a, b)
        """

    def test_add_num_and_double_raise(self):
        cal = practice2_unitest.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double('1', '1')
        # test 성공 여부를 나타냄 예외가 잘 처리 된걸로 판별


if __name__ == '__main__':
    unittest.main()
