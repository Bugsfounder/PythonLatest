marks = {"bugs": 78, "manisha": 43, "kosu": 76, 0: 32}

print(marks.items())
print(marks.keys())
marks.update({"bugs": 90, "new": 100})
print(marks)

print(marks.get("kosu"))

# What are the Difference ?
print(marks.get("noEntry"))  # it will print  None
print(marks["noEntry"])  # it will throw error
