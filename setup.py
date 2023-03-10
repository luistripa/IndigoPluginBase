from setuptools import setup, find_packages

setup(
    name='indigo',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='The Unlicense',
    author='Luis Tripa',
    author_email='',
    description='Clone of the Indigo Python API to assist IDE code completion',
    install_requires=['deprecation'],
    python_requires='>=3.6',
)
