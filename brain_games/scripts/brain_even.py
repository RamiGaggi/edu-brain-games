#!/usr/bin/env python

"""Brain games main script."""

from brain_games.games.even import even_game
from brain_games.prints import welcome_user


def main():
    """Start main."""
    name = welcome_user()
    even_game(name)


if __name__ == '__main__':
    main()
