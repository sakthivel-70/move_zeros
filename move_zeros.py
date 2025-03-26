def move_zeros(a):
    b=0
    for i in range(len(a)):
        if a[i]!=0:
            a[i],a[b]=a[b],a[i]
            b+=1
    return a
a=[2,0,8,0,5,0,3]    
print(move_zeros(a))        
