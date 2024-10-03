makeup_box = ["lipstick", "eye liner", "eye shadow", "blush", "face powder"]
print(makeup_box)

for item in makeup_box:
    if item == "lipstick":
        print("I have a red " + item)
    elif item == "eye liner":
        print("My " + item + " is black")
    elif item == "eye shadow":
        print("My " + item + " is very nice")
    else:
        print("I have " + item)
