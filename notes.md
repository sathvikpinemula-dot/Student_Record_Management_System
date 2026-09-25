# Module 2 – Functions, Files & Exception Handling

## Functions
Functions group reusable code. Parameters receive input and return values send results back.

## Lambda Functions
A lambda is a small anonymous function. Example:

```python
square = lambda x: x * x
```

## List Comprehensions
List comprehensions provide a compact way to create lists.

```python
even_numbers = [x for x in numbers if x % 2 == 0]
```

## File Handling
Python can read and write files using `open()` with modes such as `r`, `w`, and `a`.

## CSV
The `csv` module is used to read and write comma-separated data.

## JSON
The `json` module converts Python objects to JSON and reads JSON files.

## Exception Handling
`try` contains code that may fail, while `except` handles errors. `finally` is used for cleanup code that should run regardless of whether an error occurred.

## Virtual Environment
A virtual environment keeps project dependencies isolated from the system Python installation.

Example:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```
