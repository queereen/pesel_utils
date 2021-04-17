from setuptools import setup, find_packages

setup(
    name='pesel_utils',
    version='1.0',
    description='Utilities for checking PESEL numbers',
    long_description=open('README.md').read(),
    license='Hippocratic License 2.1',
    url='https://github.com/queereen/pesel_utils',
    author='Avis Drożniak',
    author_email='queereen@riseup.net',
    packages=find_packages(),
    install_requires=['numpy']
    )
