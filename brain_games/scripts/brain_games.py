#!/usr/bin/env python

"""Brain games main script."""

from brain_games.cli import welcome_user


def main():
    """Start main."""
    print('Welcome to the Brain Games!')
    print('Hello, {0}!'.format(welcome_user()))


if __name__ == '__main__':
    main()
