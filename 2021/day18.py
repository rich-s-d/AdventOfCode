
# again, short on time but found this fantastic response on reddit to learn from. 
# the answer changed multiplication to subtraction to get equal precendence (part 1), but changed substraction to be multiplication in the class. Great idea!
# same approach in part2.

# take homes: re.sub(pattern, replacement(/1), string) (/1) will give the original string back in the replacement.
#             fr, an f string literal
#             

import re
from typing import Any, Dict, Type


class Part1Number(int):
    def __add__(self, other):
        return Part1Number(super().__add__(other))

    def __sub__(self, other):
        return Part1Number(super().__mul__(other))


class Part2Number(int):
    def __add__(self, other):
        return Part2Number(super().__mul__(other))

    def __mul__(self, other):
        return Part2Number(super().__add__(other))


def evaluate_line(line, cls, replacements):
    print(line)
    print('')
    line = re.sub('([0-9]+)', fr'{cls.__name__}(\1)', line)
    print(line)
    print(cls.__name__)
    print(fr'{cls.__name__}(\1)')
    line = ''.join(replacements.get(c) for c in line)
    print(' ')
    print(line)
    print(' ')
    return eval(line)

with open('day18.txt') as f:
    lines = f.read().splitlines()
    
    print(sum(evaluate_line(line, Part1Number, {"*": "-"}) for line in lines))
    #print(sum(evaluate_line(line, Part2Number, {"*": "+", "+": "*"}) for line in lines))

#4940631886147
#283582817678281