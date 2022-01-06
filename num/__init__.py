import typing as t
import functools
import math
import enum

# NOTE: This should inherit from `int` (instead of using .value)
class Integer:
    def __init__(self, value: int, /, *, base: int = 10):
        self.value = value
        self.base = base
        # NOTE: Implement .sign:Sign ? (for +ve & -ve nums)

    def __getitem__(self, item: t.Union[int, slice]):
        digits = separate(self.value, base=self.base)[item]

        if isinstance(item, slice):
            return join(digits, base=self.base)

        return digits

    def __len__(self) -> int:
        return length(self.value, base=self.base)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.value}, base={self.base})"

    def __str__(self) -> str:
        # TODO: (e.g. return hex string, use unicode for base-n support?, implement string(n, base))
        # NOTE: What about negatives (e.g. '-1011' ?)
        raise NotImplementedError

    def __iter__(self) -> t.Iterable:
        return iter(separate(self.value, base=self.base))


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

    if {sign(a), sign(b)} == {Sign.POSITIVE, Sign.NEGATIVE}:
        raise ValueError("a and b are of incompatible signs (+ve and -ve)")

    multiplier: Sign = (
        Sign.NEGATIVE if is_negative(a) or is_negative(b) else Sign.POSITIVE
    )

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
    return abs(n)


def negative(n: int, /) -> int:
    return -abs(n)


def toggle(n: int, /) -> int:
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

    true_index = -index - 1

    if index >= 0:
        true_index += length(abs(integer), base=base)

    if not 0 <= true_index < length(abs(integer), base=base):
        raise IndexError("index out of range")

    return ((abs(integer) // (base ** true_index)) % base) * sign(integer)


def convert(integer: int, base: int, /) -> int:
    """
    Convert `integer` from base-10 to `base`

    E.g:
        >>> convert(1011, 2) == 0b1011
        True
        >>> convert(257, 8) == 0o257
        True
        >>> convert(1234, 16) == 0x1234
        True
    """

    # TODO: Make this support `from_base` and `to_base`
    # E.g:
    #   >>> convert(0x1011, from_base=16, to_base=2)
    #   0b1011

    return sum(weight(reversed(separate(integer)), base=base))

def string(integer: int, /, *, base: int = 10) -> str:
    """
    Stringify an integer

    E.g:
        >>> string(0xff, base=16)
        'ff'
    """

    # NOTE: Use `base64` for defined bases (32, 64, ...) and `uuencode` for the rest?

    raise NotImplementedError

def unstring(string: str, /, *, base: int = 10) -> int:
    """
    Un-Stringify an integer

    E.g:
        >>> unstring('ff', base=16)
        0xff
    """

    raise NotImplementedError

def lshift(integer: int, amount: int, /, *, base: int = 10) -> int:
    """
    Left-shift an integer

    E.g:
        >>> lshift(1, 2)
        100
        >>> lshift(0xabc, 1, base=16)
        0xabc0
    """

    raise NotImplementedError

def rshift(integer: int, amount: int, /, *, base: int = 10) -> int:
    """
    Right-shift an integer

    E.g:
        >>> rshift(100, 1)
        10
        >>> rshift(0xabc0, 1, base=16)
        0xabc
    """

    raise NotImplementedError