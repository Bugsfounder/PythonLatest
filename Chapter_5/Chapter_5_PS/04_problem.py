s = set()
s.add(20)
s.add(20.0)  # it doesn't count because 20.0 == 20
# s.add(20.4)  # it counts because 20.4 != 20
s.add("20")

print(len(s))
