def my_function():
    print("universe")
my_function()

def my_function(planets):
    print(planets + " solar system")
my_function("earth")
my_function("jupiter")
my_function("saturn")

def my_function(planets, solar):
    print(planets + " " + solar)
my_function("jupiter", "earth")

def my_function(*planets):
    print("the largest solar system is " + planets[1])
my_function("mars", "jupiter", "venus")

def my_function(makeup):
    for items in makeup:
        print(items)
lipstick = ["mac", "revlon", "dior"]
my_function(lipstick)

def my_function(numbers):
    return 3 * numbers

print(my_function(4))
print(my_function(5))
print(my_function(6))

def my_function(num):
    print(num)
my_function(num = 5)

def my_function(num, /):
    print(num)
my_function(4)

def my_function(*, num):
    print(num)
my_function(num = 2)

def my_function(num):
    print(num)
my_function(1)

def my_function(m, n, /, *, o, p):
    print(m + n + o + p)
my_function(2, 12, o = 3, p = 6)

def my_function(fruits = "pears"):
    print(" i love to eat " + fruits + ".")
my_function("orange")
my_function("apple")
my_function("watermelon")
my_function()

def tri_recursion(r):
  if(r > 0):
    result = r + tri_recursion(r - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(7)

