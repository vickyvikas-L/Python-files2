def flatten (ls):
    rs=[]
    for ele in ls:
        if isinstance (ele,list):
            rs.extend(flatten(ele))
        else:
            rs.append(ele)
    return rs

nlist=[1,[2,3,4],5,7,[[5,[6,7],8],9,8],4]
print(nlist)
res=flatten(nlist)
print(res)