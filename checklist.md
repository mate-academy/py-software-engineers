# Сheck Your Code Against the Following Points

1. Use the `extend()` method or `+=` operator to add multiple values to a single list.

Good example:

```python
numbers = [1, 2, 3]
numbers.extend([4, 5])
```

Also good example:

```python
numbers = [1, 2, 3]
numbers += [4, 5]
```

Bad example:

```python
numbers = [1, 2, 3]
numbers.append(4)
numbers.append(5)
```

2. `skills` variable should be an attribute of the instance not class.
3. Make sure not to override a method, if you do not add additional logic inside (that would be a bad practice).
