from setuptools import setup, find_packages

setup(
    name='alphavantage_wrapper',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python wrapper for the Alpha Vantage API',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/cchave17/alphavantage_wrapper',
    author='Your Name',
    author_email='cycvez@gmail.com'
)