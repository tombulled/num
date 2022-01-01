import typing as t
import functools
import math


class Integer:
    def __init__(self, value: int, /, *, base: int = 10):
        self.value = value
        self.base = base
        # NOTE: Implement .sign ? (for +ve & -ve nums)

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
        raise NotImplementedError  # TODO: (e.g. return hex string, use unicode for base-n support?, implement string(n, base))

    def __iter__(self) -> t.Iterable:
        return iter(separate(self.value, base=self.base))


def length(integer: int, /, *, base: int = 10) -> int:
    """
    Count the number of digits in `integer`

    E.g:
        >>> length(1234)
        4
        >>> length(0xdeadbeef, base=16)
        8
    """

    # NOTE: What about negative numbers? (give length as negative?)

    if integer == 0:
        return 1

    return math.floor(math.log(integer, base) + 1)


def separate(integer: int, /, *, base: int = 10) -> t.List[int]:
    """
    Separate the digits of `integer`

    E.g:
        >>> separate(1234)
        [1, 2, 3, 4]
        >>> separate(0xdead, base=16)
        [0xd, 0xe, 0xa, 0xd]
    """

    # TODO: Implement `weight` kwarg, such that sum(separate(integer, weight=True)) == join(separate(integer))
    # E.g:
    #   >>> separate(1234)
    #   [1, 2, 3, 4]
    #   >>> separate(1234, weight=True)
    #   [1000, 200, 30, 4]

    digits: t.List[int] = []

    index: int
    for index in range(length(integer, base=base) - 1, -1, -1):
        multiplier: int = base ** index
        digit: int = integer // multiplier

        integer -= digit * multiplier

        digits.append(digit)

    return digits


def join(integers: t.List[int], /, *, base: int = 10) -> int:
    """
    Join a list of integers into a single integer

    E.g:
        >>> join([1, 2, 3, 4])
        1234
        >>> join([0xd, 0xe, 0xa, 0xd], base=16)
        0xdead
    """

    return functools.reduce(
        lambda a, b: a * base ** length(b, base=base) + b,
        integers,
    )
