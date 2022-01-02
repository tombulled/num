import typing as t
import functools
import math
import enum


class Sign(int, enum.Enum):
    POSITIVE: int = 1
    NEGATIVE: int = -1


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


def signify(integer: int, /) -> Sign:
    """
    Signify `integer`

    E.g:
        >>> signify(-1234)
        <Sign.NEGATIVE: -1>
        >>> signify(1234)
        <Sign.POSITIVE: 1>
        >>> signify(0)
        <Sign.POSITIVE: 1>
    """

    if integer < 0:
        return Sign.NEGATIVE

    # The special case of 0 is given a +ve sign as both +ve and -ve are technically correct
    return Sign.POSITIVE


def length(
    integer: int, /, *, base: int = 10, sign: bool = False, minify: bool = False
) -> int:
    """
    Count the number of digits in `integer`

    E.g:
        >>> length(1234)
        4
        >>> length(0xdeadbeef, base=16)
        8
        >>> length(-1234, sign=True)
        -4
        >>> length(0, minify=True)
        0
    """

    # The integer 0 can be configured to be considered of
    # zero-length using `minify`
    if integer == 0:
        if minify:
            return 0
        else:
            return 1

    length: int = math.floor(math.log(abs(integer), base) + 1)

    # Negative numbers can be configured to return a negative
    # length using `sign`
    if sign:
        length *= signify(integer)

    return length


def separate(
    integer: int, /, *, base: int = 10, weight: bool = False, sign: bool = False
) -> t.List[int]:
    """
    Separate the digits of `integer`

    E.g:
        >>> separate(1234)
        [1, 2, 3, 4]
        >>> separate(0xdead, base=16)
        [0xd, 0xe, 0xa, 0xd]
        >>> separate(1234, weight=True)
        [1000, 200, 30, 4]
        >>> separate(-1234, sign=True)
        [-1, -2, -3, -4]
    """

    digits: t.List[int] = []
    signifier: int = Sign.POSITIVE

    if sign:
        signifier = signify(integer)

    integer = abs(integer)

    index: int
    for index in range(length(integer, base=base) - 1, -1, -1):
        multiplier: int = base ** index
        digit: int = integer // multiplier

        integer -= digit * multiplier

        value: int = digit * signifier

        if weight:
            value *= multiplier

        digits.append(value)

    return digits


def join(integers: t.List[int], /, *, base: int = 10, sign: bool = False) -> int:
    """
    Join a list of integers into a single integer

    E.g:
        >>> join([1, 2, 3, 4])
        1234
        >>> join([0xd, 0xe, 0xa, 0xd], base=16)
        0xdead
         >>> join([-1, -2, -3, -4], sign=True)
        -1234
    """

    signifier: int = Sign.POSITIVE

    if sign:
        # Sign must be maintained, therefore if any of the integers
        # are negative, this sign must be used
        for integer in integers:
            signifier = signify(integer)

            if signifier == Sign.NEGATIVE:
                break

    return (
        functools.reduce(
            lambda a, b: abs(a) * base ** length(b, base=base) + abs(b),
            integers,
        )
        * signifier
    )
