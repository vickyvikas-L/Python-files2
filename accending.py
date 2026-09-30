value=input('enter three integer').split(' ')
print(value)
x=(value[0])
y=(value[1])
z=(value[2])

big=x
if y>big:
    big=y
if z>big:
    big=z

small=x
if y<small:
    small=y
if z<small:
    small=z
mid=(x+y+z)-(big+small)
print('Accending:',small,mid,big)
print('Decending:',big,mid,small)