import typing as t
import functools
import math
import enum

class Integer(int):
    def __getitem__(self, item: t.Union[int, slice]):
        digits = separate(self)[item]

        if isinstance(item, slice):
            return join_all(digits)

        return digits

    def __len__(self) -> int:
        return length(self)

    def __iter__(self) -> t.Iterable:
        return iter(separate(self))


def sign(integer: int, /) -> int:
    """
    Get the sign of `integer`

    E.g:
        >>> sign(1234)
        1
        >>> sign(-1234)
        -1
        >>> sign(0)
        0
    """

    if integer == 0:
        return integer

    return integer // abs(integer)


def length(integer: int, /, *, base: int = 10) -> int:
    """
    Count the number of digits in `integer`

    E.g:
        >>> length(1234)
        4
        >>> length(0xdeadbeef, base=16)
        8
        >>> length(-1234)
        -4
        >>> length(0)
        1
    """

    if integer == 0:
        return 1

    return math.floor(math.log(abs(integer), base) + 1) * sign(integer)


def separate(integer: int, /, *, base: int = 10) -> t.List[int]:
    """
    Separate the digits of `integer`

    E.g:
        >>> separate(1234)
        [1, 2, 3, 4]
        >>> separate(0xdead, base=16)
        [0xd, 0xe, 0xa, 0xd]
        >>> separate(-1234)
        [-1, -2, -3, -4]
    """

    return [
        ((abs(integer) // (base ** index)) % base) * sign(integer)
        for index in range(length(abs(integer), base=base) - 1, -1, -1)
    ]


def join(a: int, b: int, /, *, base: int = 10) -> int:
    """
    Join two integers

    E.g:
        >>> join(12, 34)
        1234
        >>> join(-12, -34)
        -1234
    """

    signs: t.Set[int] = {sign(a), sign(b)}

    if signs == {1, -1}:
        raise ValueError("a and b are of incompatible signs (+ve and -ve)")

    multiplier: int = sign(sum(signs))

    return (abs(a) * base ** length(abs(b), base=base) + abs(b)) * multiplier


def join_all(integers: t.Iterable[int], /, *, base: int = 10) -> int:
    """
    Join an iterable of integers into a single integer

    E.g:
        >>> join([1, 2, 3, 4])
        1234
        >>> join([0xd, 0xe, 0xa, 0xd], base=16)
        0xdead
        >>> join([-1, -2, -3, -4])
        -1234
    """

    integers: t.Tuple[int] = tuple(integers)

    if len(integers) == 0:
        raise ValueError("no integers to join")
    if len(integers) == 1:
        return integers[0]

    return functools.reduce(functools.partial(join, base=base), integers)


def weight(integers: t.Iterable[int], /, *, base: int = 10) -> t.List[int]:
    """
    Weight integers

    E.g:
        >>> weight([1, 2, 3, 4])
        [1, 20, 300, 4000]
    """

    return [
        integer * base ** index
        for index, integer in enumerate(integers)
    ]


def positive(n: int, /) -> int:
    """
    Convert `n` to its positive form: |n|

    E.g:
        >>> positive(123)
        123
        >>> positive(-123)
        123
    """

    return abs(n)


def negative(n: int, /) -> int:
    """
    Convert `n` to its negative form: -|n|

    E.g:
        >>> negative(123)
        -123
        >>> negative(-123)
        -123
    """

    return -abs(n)


def toggle(n: int, /) -> int:
    """
    Toggle the sign of `n`

    E.g:
        >>> toggle(123)
        -123
        >>> toggle(-123)
        123
    """

    return -n


def get(integer: int, index: int, /, *, base: int = 10) -> int:
    """
    Retrieve the integer at a specific index in `integer`

    E.g:
        >>> get(1234, 0)
        1
        >>> get(1234, -1)
        4
    """

    true_index: int = -index - 1

    if index >= 0:
        true_index += length(abs(integer), base=base)

    if not 0 <= true_index < length(abs(integer), base=base):
        raise IndexError("index out of range")

    return ((abs(integer) // (base ** true_index)) % base) * sign(integer)


def convert(integer: int, /, *, from_base: int = 10, to_base: int = 10) -> int:
    """
    Convert `integer` from base `from_base` to base `to_base`

    E.g:
        >>> convert(1011, to_base=2)
        0b1011
        >>> convert(0x789, from_base=16)
        789
        >>> convert(0x1011, from_base=16, to_base=2)
        0b1011
    """

    digits: t.List[int] = separate(integer, base=from_base)

    digit: int
    for digit in digits:
        if digit > to_base - 1:
            raise Exception(f'{digit} is an invalid base-{to_base} integer')

    return join_all(digits, base=to_base)

def shift(integer: int, /, *, amount: int = 1, base: int = 10) -> int:
    """
    Shift an integer

    E.g:
        >>> shift(123, amount=2)
        12300
        >>> shift(-123, amount=-2)
        -1
        >>> shift(0xabc, base=16)
        0xabc0
        >>> shift(123, amount=-1)
        12
        >>> shift(0xabc0, amount=-1, base=16)
        0xabc
    """

    if amount > 0:
        return join_all(separate(integer, base=base) + [0] * amount, base=base)
    elif amount < 0:
        return join_all(separate(integer, base=base)[:amount], base=base)

    return amount