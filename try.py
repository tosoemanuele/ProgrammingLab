def funz(pipo):
    tmp=[]
    
    for i in range(len(pipo)):
        if pipo[i] in range(-2,3):
            tmp.append(pipo[i])
    return tmp


app = funz([-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
print(app)