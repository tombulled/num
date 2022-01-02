import num

assert num.signify(-1234) == -1
assert num.signify(1234) == 1

assert num.length(0) == 1
assert num.length(0, minify=True) == 0
assert num.length(-1234) == 4
assert num.length(-1234, sign=True) == -4
assert num.length(1) == 1
assert num.length(1234) == 4
assert num.length(0xdead, base=16) == 4

assert num.join([1, 2, 3, 4]) == 1234
assert num.join([4, 3, 2, 1]) == 4321
assert num.join([0xd, 0xe, 0xa, 0xd], base=16) == 0xdead
assert num.join([0xbe, 0xef], base=16) == 0xbeef
assert num.join([0o2, 0o5, 0o7], base=8) == 0o257
assert num.join([0b1, 0b1, 0b0], base=2) == 0b110
assert num.join([-1, -2, -3, -4], sign=True) == -1234
assert num.join([-1, 2, 3, 4], sign=True) == -1234
assert num.join([-1, 2, 3, 4], sign=False) == 1234
assert num.join([0, 0, 0]) == 0
assert num.join([123, 456, 789]) == 123456789

assert num.separate(1234) == [1, 2, 3, 4]
assert num.separate(4321) == [4, 3, 2, 1]
assert num.separate(0xdead, base=16) == [0xd, 0xe, 0xa, 0xd]
assert num.separate(0xbeef, base=16) == [0xb, 0xe, 0xe, 0xf]
assert num.separate(0o257, base=8) == [0o2, 0o5, 0o7]
assert num.separate(0b1011, base=2) == [0b1, 0b0, 0b1, 0b1]
assert num.separate(-1234) == [1, 2, 3, 4]
assert num.separate(-1234, sign=False) == [1, 2, 3, 4]
assert num.separate(-1234, sign=True) == [-1, -2, -3, -4]
assert num.separate(1234, weight=True) == [1000, 200, 30, 4]
assert num.separate(-1234, weight=True, sign=True) == [-1000, -200, -30, -4]

i = num.Integer(1234)

assert i[0] == 1
assert i[::-1] == 4321
assert i[:2] == 12
assert len(i) == 4
assert list(i) == [1, 2, 3, 4]

print('All tests passed.')