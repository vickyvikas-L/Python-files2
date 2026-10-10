num=int(input('enter the number'))
freq={}
while num!=0:
    d=num%10
    freq[d]=freq.get(d,0)+1
    num=num//10
    
print(freq)