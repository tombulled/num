import num

integer = num.Integer(1234)

assert num.positive(123) == 123
assert num.positive(-123) == 123

assert num.negative(-123) == -123
assert num.negative(123) == -123

assert num.toggle(123) == -123
assert num.toggle(-123) == 123

assert num.sign(-1234) == -1
assert num.sign(1234) == 1

assert num.join(123, 456) == 123456
assert num.join(0, 123) == 123
assert num.join(123, 0) == 1230
assert num.join(0, 0) == 0
assert num.join(-123, -456) == -123456
assert num.join(0, -123) == -123
assert num.join(-123, 0) == -1230

assert num.length(0) == 1
assert num.length(1) == 1
assert num.length(1234) == 4
assert num.length(-1234) == -4
assert num.length(0xdead, base=16) == 4
assert num.length(-0xdead, base=16) == -4

assert num.join_all([1, 2, 3, 4]) == 1234
assert num.join_all([4, 3, 2, 1]) == 4321
assert num.join_all([0xd, 0xe, 0xa, 0xd], base=16) == 0xdead
assert num.join_all([0xbe, 0xef], base=16) == 0xbeef
assert num.join_all([0o2, 0o5, 0o7], base=8) == 0o257
assert num.join_all([0b1, 0b1, 0b0], base=2) == 0b110
assert num.join_all([-1, -2, -3, -4]) == -1234
assert num.join_all([0, 0, 0]) == 0
assert num.join_all([123, 456, 789]) == 123456789

assert num.separate(1234) == [1, 2, 3, 4]
assert num.separate(4321) == [4, 3, 2, 1]
assert num.separate(0xdead, base=16) == [0xd, 0xe, 0xa, 0xd]
assert num.separate(0xbeef, base=16) == [0xb, 0xe, 0xe, 0xf]
assert num.separate(0o257, base=8) == [0o2, 0o5, 0o7]
assert num.separate(0b1011, base=2) == [0b1, 0b0, 0b1, 0b1]
assert num.separate(-1234) == [-1, -2, -3, -4]

assert num.convert(1011, to_base=2) == 0b1011
assert num.convert(257, to_base=8) == 0o257
assert num.convert(1234, to_base=16) == 0x1234
assert num.convert(0b1011, from_base=2) == 1011
assert num.convert(0o257, from_base=8) == 257
assert num.convert(0x789, from_base=16) == 789
assert num.convert(0x1011, from_base=16, to_base=2) == 0b1011

assert num.shift(123, amount=2) == 12300
assert num.shift(0xabc, base=16) == 0xabc0
assert num.shift(100, amount=-1) == 10
assert num.shift(0xabc0, amount=-1, base=16) == 0xabc

assert integer[0] == 1
assert integer[:2] == 12
assert integer[::-1] == 4321
assert len(integer) == 4
assert list(integer) == [1, 2, 3, 4]

print('All tests passed.')