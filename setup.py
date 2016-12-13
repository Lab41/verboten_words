from setuptools import find_packages
from setuptools import setup

setup(
    name='verboten_words',
    description='no naughty words in the repo',
    url='https://github.com/Lab41/verboten_words.git',
    version='1.0.0',
    author='dgrossman',
    author_email='dgrossman@iqt.org',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages(exclude=('tests*', 'testing*')),
    entry_points={
        'console_scripts': [
            'verboten-words = verboten_words.verboten_words:verboten_words',
        ],
    },
)
