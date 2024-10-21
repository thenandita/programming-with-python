x = {"audi", "ford", "ferrari"}
print(type(x))

x = {"audi", "ford", "ferrari"}
print(len(x))

x = {"audi", "ford", "ferrari, tesla", "audi"}
print(x)

x = {"audi", "ford", "ferrari"}
print("audi" in x)

x = {"audi", "ford", "ferrari"}
x.add("tesla")
print(x)

x = {"audi", "ford", "ferrari"}
y = {"tesla", "honda", "mazda"}
x.update(y)
print(x)

x = {"audi", "ford", "ferrari"}
y = {1, 3, 5}
z = x.union(y)
print(z)

x = {"audi", "ford", "ferrari"}
y = {1, 3, 5}
z = x | y
print(z)

a = {"audi", "ford", "ferrari"}
b = {1, 3, 5}
c = {"aa", "ab", "ac"}
d = {"speed", "limit"}
e = a.union(b, c, d)
print(e)

a = {"audi", "ford", "ferrari"}
b = (1, 3, 5)
c = a.union(b)
print(c)

x = {"audi", "ford", "ferrari"}
y = {"tesla", "honda", "audi"}
My_set = x.intersection(y)
print(My_set)

x = {"audi", "ford", "ferrari"}
y = {"tesla", "honda", "audi"}
My_set = x & y
print(My_set)

x = {"audi", 1, "ferrari", 0}
y = {False, 4, "honda", True, "audi"}
z = x.intersection(y)
print(z)

x = {"audi", "ford", "ferrari"}
y = {"ford", "night queen", "rose"}
z = x.difference(y)
print(z)

x = {"audi", "ford", "ferrari"}
y = {"ford", "night queen", "rose"}
z = x - y
print(z)

x = {"audi", "ford", "ferrari"}
y = {"ford", "night queen", "rose"}
z = x.symmetric_difference(y)
print(z)

x = {"audi", "ford", "ferrari"}
y = {"ford", "night queen", "rose"}
z = x ^ y
print(z)

x = {"audi", "ford", "ferrari"}
y = {"ford", "night queen", "rose"}
z = x.symmetric_difference_update(y)
print(x)

x = {"audi", "ford", "ferrari"}
x.remove("ford")
print(x)

x = {"audi", "ford", "ferrari"}
x.clear()
print(x)

x = {"audi", "ford", "ferrari"}
x.pop()
print(x)

x = {"audi", "ford", "ferrari"}
x.discard("ford")
print(x)