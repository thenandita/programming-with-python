veg_list = ["onion", "cabbage", "potato"]
print(len(veg_list))

list5 = ["onion", "cabbage", "potato"]
list6 = [6, 7, 8, 9, 2]
list7 = [False, True, False]

print(list5)
print(list6)
print(list7)

veg_list = ["onion", "cabbage", "potato"]
print(type(veg_list))

veg_list = ["onion", "cabbage", "potato"]
print(veg_list[-2])

veg_list = ["onion", "cabbage", "potato", "spinach"]
print(veg_list[1]) # first item index 0

veg_list = ["onion", "cabbage", "potato", "spinach", "broccoli", "carrot", "corn"]
print(veg_list[2:5])

veg_list = ["onion", "cabbage", "potato", "spinach"]
print(veg_list)
veg_list.append("tomato")
print(veg_list)

veg_list = ["onion", "cabbage", "potato", "spinach", "tomato",]
veg_list.insert(3, "corn")
print(veg_list)

veg_list = ["onion", "cabbage", "potato"]
add = ["corn", "tomato", "cauliflower"]
veg_list.extend(add)
print(veg_list)

veg_list = ["onion", "cabbage", "potato"]
veg_list.remove("onion")
print(veg_list)

veg_list = ["onion", "cabbage", "potato"]
veg_list.pop()
print(veg_list)

veg_list = ["onion", "cabbage", "potato"]
del veg_list[0]
print(veg_list)

veg_list = ["onion", "cabbage", "potato"]
veg_list.clear()
print(veg_list)