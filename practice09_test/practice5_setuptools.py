from setuptools import setup, find_packages

setup(
    name='python_programming_demo_app',
    version='0.0.2',
    packages=find_packages(),  # 자신이 찾아서 package 화 하는 것을 한다
    package_data={'roboter': ['templates/*.txt']},
    url='http://test.test.com',
    listense='MIT',
    author='test',
    athor_email='example@example.com',
    install_requires=['termcolor==1.1.0'],
    description='roboter description',
    test_suits='tests',  # test file 을 지정 하는 부분 -> 해당 file이 존재 해야 한다
)  # unitest일 경우는 이렇게 하고
# pytest일 경우 cfg라는 파일을 만들어서 거기에 해당 경로 설정을 한 후 해야한다
