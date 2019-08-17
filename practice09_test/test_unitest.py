import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC  # 대기 시간 설정
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        self.driver.get('http://www.python.org')
