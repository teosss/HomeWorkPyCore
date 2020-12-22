# Color Ghost
# https://www.codewars.com/kata/color-ghost

from random import choice

class Ghost(object):
    def __init__(self):
        self.color = choice(["white", "yellow", "purple", "red"])