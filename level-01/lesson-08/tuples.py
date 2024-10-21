from itertools import count

my_tuple = ("corn", "tomato", "cabbage", "potato", "tomato")
print(my_tuple)

my_tuple = ("corn", "tomato", "cabbage")
print(len(my_tuple))

my_tuple = (8, "true", 24, "tomato")
print(my_tuple)

my_tuple = ("corn", "tomato", "cabbage", "potato", "carrot")
print(my_tuple[1:3])

my_tuple = ("corn", "tomato", "cabbage", "potato", "carrot")
print(my_tuple[:4])

my_tuple = ("corn", "tomato", "cabbage", "potato", "carrot", "spinach")
print(my_tuple[3:])

my_tuple = ("corn", "tomato", "cabbage", "potato", "carrot", "spinach", "broccoli")
print(my_tuple[-5:-2])

my_tuple = ("corn", "tomato", "cabbage", "potato", "carrot", "spinach", "broccoli")
print(my_tuple[1:2])

my_tuple = ("corn", "tomato", "cabbage")
if "tomato" in my_tuple:
    print("true")

my_tuple = ("corn", "tomato", "cabbage")
veg = list(my_tuple)
veg[0] = "broccoli"
my_tuple = tuple(veg)

print(my_tuple)

my_tuple = ("corn", "tomato", "cabbage")
veg = list(my_tuple)
veg.append("carrot")
my_tuple = tuple(veg)

print(my_tuple)

my_tuple = ("corn", "tomato", "cabbage")
veg = ("potato",)
my_tuple += veg

print(my_tuple)

my_tuple = ("corn", "tomato", "cabbage")
veg = list(my_tuple)
veg.remove("corn")
my_tuple = tuple(veg)

print(my_tuple)

veg = ("corn", "tomato", "cabbage")
(boil, curry, fry) = veg
print(fry)

veg = ("corn", "tomato", "cabbage", "carrot", "broccoli")
(boil, curry, *fry) = veg
print(boil)
print(curry)
print(fry)

veg = ("corn", "tomato", "cabbage", "carrot", "broccoli")
(*boil, curry, fry) = veg
print(boil)
print(curry)
print(fry)

veg_tuple = (
    "corn",
    "tomato",
    "cabbage",
)
veg2_tuple = ("carrot", "broccoli", "spinach")

veg3_tuple = veg_tuple + veg2_tuple
print(veg3_tuple)

veg = (
    "corn",
    "tomato",
    "cabbage",
)
my_tuple = veg * 2
print(my_tuple)

my_tuple = ("corn", "tomato", "cabbage", "tomato", "potato", "tomato")
veg = my_tuple.count("tomato")
print(veg)

my_tuple = ("corn", "cabbage", "tomato", "potato", "tomato")
veg = my_tuple.index("tomato")
print(veg)

my_tuple = ("corn", "cabbage", "tomato", "potato", "radish")
for veg in range(len(my_tuple)):
    print(my_tuple[veg])

my_tuple = ("corn", "cabbage", "tomato", "potato", "radish")
veg = 1
while veg < len(my_tuple):
    print(my_tuple[veg])
    veg = veg + 3
