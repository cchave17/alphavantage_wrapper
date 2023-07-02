from setuptools import setup, find_packages

setup(
    name='alphavantage_wrapper',
    version='0.1.0',
    license='MIT',
    description='A Python wrapper for the Alpha Vantage API',
    long_description=open('README.md').read(),
    url='https://github.com/cchave17/alphavantage_wrapper',
    author='Carlos Chavez',
    author_email='cycvez@gmail.com',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'requests',
        'pandas'
    ],
)