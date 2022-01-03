# num
Integer utility library

## Usage

### Sign
```python
>>> num.signify(-1234)
<Sign.NEGATIVE: -1>
>>> num.signify(1234)
<Sign.POSITIVE: 1>
```

### Length
```python
>>> num.length(1234)
4
>>> num.length(0xdeadbeef, base=16)
8
>>> num.length(-1234, sign=True)
-4
>>> num.length(0, minify=True)
0
```

### Separate
```python
>>> num.separate(1234)
[1, 2, 3, 4]
>>> num.separate(0xdead, base=16)
[0xd, 0xe, 0xa, 0xd]
>>> num.separate(1234, weight=True)
[1000, 200, 30, 4]
>>> num.separate(-1234, sign=True)
[-1, -2, -3, -4]
>>> num.separate(-1234, weight=True, sign=True)
[-1000, -200, -30, -4]
```

### Join
```python
>>> num.join([1, 2, 3, 4])
1234
>>> num.join([0xd, 0xe, 0xa, 0xd], base=16)
0xdead
>>> num.join([-1, -2, -3, -4], sign=True) 
-1234
```