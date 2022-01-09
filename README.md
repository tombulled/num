# num
Integer utility library

## Usage

### `sign`
Get the sign of an integer

```python
>>> num.sign(1234)
1
>>> num.sign(-1234)
-1
>>> num.sign(0)
0
```

### `length`
Count the number of digits in an integer

```python
>>> num.length(1234)
4
>>> num.length(-1234)
-4
>>> num.length(0xdeadbeef, base=16)
8
```

### `separate`
Separate the digits of an integer

```python
>>> num.separate(1234)
[1, 2, 3, 4]
>>> num.separate(-1234)
[-1, -2, -3, -4]
>>> num.separate(0xdead, base=16)
[0xd, 0xe, 0xa, 0xd]
```

### `join`
Join two integers

```python
>>> num.join(12, 34)
1234
>>> num.join(-12, -34) 
-1234
>>> num.join(0xde, 0xad, base=16)
0xdead
```

### `join_all`
Join an iterable of integers into a single integer

```python
>>> num.join_all([1, 2, 3, 4])
1234
>>> num.join_all([-1, -2, -3, -4]) 
-1234
>>> num.join_all([0xd, 0xe, 0xa, 0xd], base=16)
0xdead
```

### `weight`
Weight an iterable of integers

```python
>>> num.weight([1, 2, 3, 4])
[1, 20, 300, 4000]
>>> num.weight([-1, -2, -3, -4])
[-1, -20, -300, -4000]
>>> num.weight([0xa, 0xb, 0xc, 0xd], base=16)
[0xa, 0xb0, 0xc00, 0xd000]
```

### `get`
Retrieve the integer at a specific index in an integer

```python
>>> num.get(1234, 0)
1
>>> num.get(-1234, -1)
-4
```

### `convert`
Convert an integer between bases

```python
>>> num.convert(1011, to_base=2)
0b1011
>>> num.convert(0x789, from_base=16)
789
>>> num.convert(0x1011, from_base=16, to_base=2)
0b1011
```

### `shift`
Shift an integer

```python
>>> num.shift(123, amount=2)
12300
>>> num.shift(-123, amount=-2)
-1
>>> num.shift(0xabc, base=16)
0xabc0
>>> num.shift(123, amount=-1)
12
>>> num.shift(0xabc0, amount=-1, base=16)
0xabc
```

### `positive`
Convert an integer to its positive form

```python
>>> num.positive(1234)
1234
>>> num.positive(-1234)
1234
```

### `negative`
Convert an integer to its negative form

```python
>>> num.negative(1234)
-1234
>>> num.negative(-1234)
-1234
```

### `toggle`
Toggle the sign of an integer

```python
>>> num.toggle(1234)
-1234
>>> num.toggle(-1234)
1234
```