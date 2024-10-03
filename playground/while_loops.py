makeup_box = ["lipstick", "eye liner", "eye shadow", "blush", "face powder"]

size = len(makeup_box)

print("Printing items from makeup_box")

index = 0
while index < size:
    item = makeup_box[index]
    print(item)

    if item == "blush":
        break

    index += 1

print("Printing completed")
