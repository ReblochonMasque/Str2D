from distutils.core import setup

setup(
    name='src',
    version='0.1',
    author='Sean Smith',
    author_email='pirsquared.snv@gmail.com',
    packages=['src'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.rst').read(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

)