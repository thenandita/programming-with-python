from platform import machine

my_dict = {
    "mac": "lipstick",
    "color": "brown",
}
print(my_dict)

my_dict = {
    "mac": "lipstick",
    "color": "sand nude",
    "type": "liquid"
}
print(my_dict["mac"])

my_dict = {
    "mac": "lipstick",
    "color": "brown",
}
print(type(my_dict))

my_dict = dict(brand = "toyota", model = "corolla",)
print(my_dict)

my_dict = {
    "mac": "lipstick",
    "color": "brown",
}
print(len(my_dict))

my_dict = {
    "mac": "lipstick",
    "type": "liquid",
    "colors": ["nude", "brown", "red"],
    "cases": ["square", "round"]
}
print(my_dict)

my_dict = {
    "mac": "lipstick",
    "color": "sand nude",
    "type": "liquid"
}
makeup = my_dict.get("mac")
print(makeup)

my_dict = {
    "mac": "lipstick",
    "color": "sand nude",
    "type": "liquid"
}
makeup = my_dict.keys()
print(makeup)

my_dict = {
    "mac": "lipstick",
    "type": "liquid",
    "colors": "nude"
}
makeup = my_dict.keys()
print(makeup) # before change

my_dict["shape"] = "round"
print(makeup) # after change

my_dict = {
    "mac": "lipstick",
    "type": "liquid",
    "colors": "nude"
}
if "type" in my_dict:
    print("yes")

my_dict = {
    "mac": "lipstick",
    "type": "liquid",
    "colors": "nude"
}
makeup = my_dict.items()
print(makeup) # before change

my_dict["shape"] = "round"
print(makeup) # after change

my_dict = {
    "mac": "lipstick",
    "type": "liquid",
    "shade": "14"
}
makeup = my_dict.items()
print(makeup) # before change
my_dict["shade"] = 20
print(makeup) # after change

my_dict = {
    "mac": "lipstick",
    "type": "liquid",
    "colors": "red"
}
my_dict.update({"colors": "pink"})
print(my_dict)

my_dict = {
    "mac": "lipstick",
    "type": "liquid",
    "colors": "red"
}
my_dict.pop("mac")
print(my_dict)

my_dict = {
    "mac": "lipstick",
    "type": "liquid",
    "colors": "red"
}
makeup = my_dict.copy()
print(makeup)

makeup = dict(my_dict)
print(makeup)

my_dict = {
    "mac": "lipstick",
    "type": "liquid",
    "colors": "red"
}
for makeup in my_dict:
    print(makeup)

for makeup in my_dict:
    print(my_dict[makeup])

my_dict = {
    "mac": "lipstick",
    "type": "liquid",
    "colors": "red"
}
for makeup in my_dict.values():
    print(makeup)

for makeup in my_dict.keys():
    print(makeup)

for makeup, values in my_dict.items():
    print(makeup, values)

Lipstick = {
    "mac": {
        "color" : "rose gold",
        "shade" : 4
    },
    "dior": {
        "color" : "sand nude",
        "shade" : 13
    },
    "revlon": {
        "color" : "brown",
        "shade" : 6
    }
}
print(Lipstick)

Lipstick = {
    "mac": {
        "color" : "rose gold",
        "shade" : 4
    },
    "dior": {
        "color" : "sand nude",
        "shade" : 13
    }
}
print(Lipstick["dior"]["shade"])

