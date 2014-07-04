#try:
#    from setuptools import setup
#except ImportError:
#    from distutils.core import setup

from setuptools import setup, find_packages

setup(
    name='coursera',
    description='',
    author='coursera-dl',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'coverage',
        "html5lib",
        "nose",
        "requests",
        "six"
    ],
)
