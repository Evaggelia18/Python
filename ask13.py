def maxDistance(a,num):
    x = len(a)
    #print (x)
    length = num
    max = 0
    
    for b in range (1,x) :
        for c in range (x-1,0,-1) :
            if a[c-1]>a[c] :
                temp=a[c]
                a[c]=a[c-1]
                a[c-1]=temp
                
    for i in range(x-1,0,-1):
        if max < length and (max + a[i]) < length :
            print (a[i])
            max = max + a[i]
    print (max)


