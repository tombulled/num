import num

'''
TODO:
    * Claim PyPI name (Need v1 first)

What about class-based? (linteger, mint, )

i = Integer(1234)

len(i) == 4

i[0] == 1
'''

assert num.length(1) == 1
assert num.length(1234) == 4
assert num.length(0xdead, base=16) == 4

assert num.join([1, 2, 3, 4]) == 1234
assert num.join([4, 3, 2, 1]) == 4321
assert num.join([0xd, 0xe, 0xa, 0xd], base=16) == 0xdead
assert num.join([0xb, 0xe, 0xe, 0xf], base=16) == 0xbeef

assert num.separate(1234) == [1, 2, 3, 4]
assert num.separate(4321) == [4, 3, 2, 1]
assert num.separate(0xdead, base=16) == [0xd, 0xe, 0xa, 0xd]
assert num.separate(0xbeef, base=16) == [0xb, 0xe, 0xe, 0xf]

print('All tests passed.')

i = num.Integer(1234)

assert i[0] == 1
assert i[::-1] == 4321
assert i[:2] == 12
assert len(i) == 4
assert list(i) == [1, 2, 3, 4]