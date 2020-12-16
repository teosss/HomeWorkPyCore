# Multiples of 3 or 5
# https://www.codewars.com/kata/multiples-of-3-or-5

def solution(number):
    return sum(i for i in range(number) if i > 0 and i % 3 == 0 or i % 5 == 0)