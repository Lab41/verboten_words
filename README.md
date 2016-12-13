verboten_words
==========

Tool for automatically flagging when you use a restricted word in your code

## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Hooks available:
- `verboten-words` - This hook alerts you to files with forbidden words.


## What does it do?

Keep you from checking in files with internal naming conventions.

## what If I want my own words?

make an environment variable  `VERBOTEN_FILE`, one word per line comment lines start with a #

## what If I really really want to push something in.

make an environment variable `F_IT` and commit to your hearts content...

