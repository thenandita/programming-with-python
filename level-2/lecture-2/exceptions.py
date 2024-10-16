try:
    print(mn)
except:
    print("an error occurred")

try:
    print(mn)
except NameError:
    print("Variable not right")
except:
    print("something else")

try:
    print("hey")
except:
    print("something wrong")
else:
    print("all right")

try:
    print(m)
except:
    print("something wrong")
finally:
    print("The 'try except' is finished")