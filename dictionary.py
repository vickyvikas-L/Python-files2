str=input('enter the sentence')
words=str.split(' ')
group={}
for word in words:
    fchar=word[0]
    if fchar not in group:
        group[fchar]=[]
    group[fchar].append(word)
    
print(group)
for k , v in group.items():
    print(k,"=",v)