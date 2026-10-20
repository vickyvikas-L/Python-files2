def flatten (ls):
    rs=[]
    for ele in ls:
        if isinstance (ele,list):
            for x in ele:
                rs.append(x)
        else:
            rs.append(ele)
    return rs

nlist=[1,[2,3,4],5,7,[9,8],4]
print(nlist)
res=flatten(nlist)
print(res)