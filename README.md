# PythonLatest
Learning Latest Python

## Tuple Methods
### Indexing

```python

t = (1, 2, 3, 4)
print(t[1])  # Output: 2
```
### Slicing

```python

t = (1, 2, 3, 4, 5)
print(t[1:3])  # Output: (2, 3)
```
### Count

```python

t = (1, 2, 3, 1, 2, 1)
print(t.count(1))  # Output: 3
```
### Index

```python

t = (1, 2, 3, 4, 2)
print(t.index(2))  # Output: 1
```
### Length

```python

t = (1, 2, 3, 4)
print(len(t))  # Output: 4
```
### Concatenation

```python

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # Output: (1, 2, 3, 4)
```
### Repetition

```python

t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)
```
### Membership

```python

t = (1, 2, 3, 4)
print(2 in t)  # Output: True
print(5 in t)  # Output: False
```
### Iteration

```python
t = (1, 2, 3)
for item in t:
    print(item)
# Output:
# 1
# 2
# 3
```   
### Unpacking

```python

t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Output: 1 2 3
```

Script for run requirements.txt file without crashing 
```python
import subprocess


def install_package(package):
    try:
        subprocess.check_call(["pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Failed to install package: {package}")


def main():
    with open("sys_requirements.txt", "r") as f:
        for line in f:
            package = line.strip()
            if package and not package.startswith("#"):
                install_package(package)


if __name__ == "__main__":
    main()

```