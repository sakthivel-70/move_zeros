def move_zeros(a):
    b=0
    for i in range(len(a)):
        if a[i]!=0:
            a[i],a[b]=a[b],a[i]
            b+=1
    return a
a=[4,6,0,7,0,7,8,9,0]      

print(move_zeros(a))        
