# num
Integer utility library

## Usage

### Sign
```python
>>> num.sign(1234)
1
>>> num.sign(-1234)
-1
>>> num.sign(0)
0
```

### Length
```python
>>> num.length(1234)
4
>>> num.length(-1234)
-4
>>> num.length(0xdeadbeef, base=16)
8
```

### Separate
```python
>>> num.separate(1234)
[1, 2, 3, 4]
>>> num.separate(-1234)
[-1, -2, -3, -4]
>>> num.separate(0xdead, base=16)
[0xd, 0xe, 0xa, 0xd]
```

### Join All
```python
>>> num.join_all([1, 2, 3, 4])
1234
>>> num.join_all([-1, -2, -3, -4]) 
-1234
>>> num.join_all([0xd, 0xe, 0xa, 0xd], base=16)
0xdead
```

### Weight
```python
>>> num.weight([1, 2, 3, 4])
[1, 20, 300, 4000]
>>> num.weight([-1, -2, -3, -4])
[-1, -20, -300, -4000]
>>> num.weight([0xa, 0xb, 0xc, 0xd], base=16)
[0xa, 0xb0, 0xc00, 0xd000]
```

### Get
```python
>>> num.get(1234, 0)
1
>>> num.get(-1234, -1)
-4
```

### Positive
```python
>>> num.positive(1234)
1234
>>> num.positive(-1234)
1234
```

### Negative
```python
>>> num.negative(1234)
-1234
>>> num.negative(-1234)
-1234
```

### Toggle
```python
>>> num.toggle(1234)
-1234
>>> num.toggle(-1234)
1234
```