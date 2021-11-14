# Playground for relative imports in Python

## Running options

To avoid problems with parent imports, you can run the tests from a sibling directory (`tests/` sibling of `src/`) as follows:

```py
python -m tests.test_avengers
```

and an example "main" program as:

```py
python -m src.main
```
