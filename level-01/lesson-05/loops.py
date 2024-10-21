a = 3
while a < 6:
    print(a)
    a += 3

a = 2
while a < 10:
    print(a)
    if a == 4:
        break
    a += 2

a = 1
while a < 7:
    a += 2
    if a == 3:
        continue
    print(a)

veg = ["corn", "cauliflower", "tomato", "capsicum", "spinach"]
for pick in veg:
    print(pick)
    if pick == "tomato":
        break

veg = ["corn", "cauliflower", "tomato", "capsicum", "spinach"]
for pick in veg:
    if pick == "tomato":
        break
    print(pick)

for value in range(3, 7):
    print(value)

for value in range(3, 29, 3):
    print(value)

food = ["chicken", "mutton", "beef"]
dishes = ["curry", "steak", "kebab"]

for meats in food:
    for items in dishes:
        print(meats, items)
