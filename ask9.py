def maxSequence(li):
    x = len(li)
    max = 0
    sub_list = []
    sub_list1 = []
    sub_list2 = []
    #εδω ελεγχει ολα τα στοιχεια εκτος απο το τελευταιο για το μεγιστο αθροισμα και σε καθε επαναληξη αφαιρει ενα απο το τελος
    for a in range(1,x - 1):
        max1 = 0
        for b in range (0,x - a):
             max1 = max1 + li[b]
        if max1 > max :
            sub_list1.clear()
            max = max1
            for c in range (0,x - a):
                sub_list1.append(li[c])
    #εδω ελεγχει ολα τα στοιχεια εκτος απο το πρωτο για το μεγιστο αθροισμα και σε καθε επαναληξη αφαιρει ενα απο την αρχη
    for d in range(1,x - 1):
        max2 = 0
        for e in range (d,x):
             max2 = max2 + li[e]
        if max2 > max :
            sub_list2.clear()
            max = max2
            for f in range (d,x):
                sub_list2.append(li[f])
                
    k = int(x/2)
    for g in range (0,k):
        max3 = 0
        for h in range (1 + g, x - g):
            max3 = max3 + li[h]
        if max3 > max :
            sub_list.clear()
            max = max3
            for i in range (h,x - g):
                sub_list.append(li[i])
    #εδω ελεγχει πιο αθροισμα απ'τις δυο επαναληξεις ειναι μεγαλυτερο ωστε να εμφανισει την καταλληλη λιστα
    if (max1 > max2 and max1 > max3) :
        print ("max = ",max," sub_list1 =",sub_list1)
        #sub_list = s2b_list1
    elif (max2 > max1 and max2 > max3) :
        print ("max = ",max," sub_list2 =",sub_list2)
    else :
        print ("max = ",max," sub_list =",sub_list)
        