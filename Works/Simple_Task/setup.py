from setuptools import setup, find_packages

setup(
    name='tasks',
    version='0.0.1',
    author='Oralcoder',
    author_email='oralcoder@gmail.com',
    description='A Simple Task Management Package',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['tinydb==3.15.1', 'six'],
)