def dims(image, temp):
    if temp ==0:
        x = image.shape[0]
        y = image.shape[1]
        print(x, y)
        temp = 1
    return temp