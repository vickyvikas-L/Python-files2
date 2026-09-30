def create_array(x, y, z, value):
    arr = [[[value for k in range(z)]
            for j in range(y)]
            for i in range(x)]
    return arr

a = create_array(2, 5, 2, 5)
print(a)