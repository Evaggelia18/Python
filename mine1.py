from random import *
import random


bomb=int(input("Give a random number of bombs: " ))
h=int(input("Give the height of the board: " ))
w=int(input("Give the width of the board: " ))


#Ελεγχος ωστε ο αριθμος της βομβας να μην ξεπερνα α κελια του πινακα
while (bomb>h*w):
    print ("The number has to be smaller than ",h*w,". Please give another number: ")
    bomb=int(input())
    
print("Thank you!")

list1=["   "]    
num=[0]          #Θα χρησιμοποιηθει για τους τυχαιους αριθμους
b=[0]            #Θα χρησιμοποιηθει για να τοποθετηθουν οι αριθμοι διπλα στις βομβες
for i in range(1, h*w ):
    list1.append("   ")
    num.append(i)
    b.append(0)

for a in range(bomb):
    y=random.choice(num)
    #Ελεγχος ωστε να μην επιλεγει παραπανω απο μια φορα το ιδιο κελι
    while (list1[y]=="BOOM"):
        y=random.choice(num)
    list1[y]="BOOM"
    
#Θα ελεγχουμε τα κελια που δεν εχουν βομβες για να δουμε με ποσες βομβες ακουμπανε
for i in range (h*w):
    if (list1[i]=="   "):
        #Ελεγχος για το πρωτο κελι της πρωτης σειρας
        if (i==0):
           if (list1[i+1]=="BOOM"):
               b[i]=b[i]+1
           if (list1[i+w]=="BOOM"):
               b[i]=b[i]+1
           if (list1[i+w+1]=="BOOM"):
               b[i]=b[i]+1
               
        #Eλεγχος για το τελευταιο κελι τησ πρωτης σειρας 
        elif (i==(w-1)):
            if (list1[i-1]=="BOOM"):
                b[i]=b[i]+1
            if (list1[i+w]=="BOOM"):
                b[i]=b[i]+1
            if (list1[i+w-1]=="BOOM"):
                b[i]=b[i]+1
        #Ελεγχος της πρωτης σειρας εκτος απο τα ακριανα κελια
        elif (i>0 and i<(w-1)):
            if(list1[i-1]=="BOOM"):
                b[i]=b[i]+1
            if(list1[i+1]=="BOOM"):
                b[i]=b[i]+1
            if(list1[i+w]=="BOOM"):
                b[i]=b[i]+1
            if(list1[i+w-1]=="BOOM"):
                b[i]=b[i]+1
            if(list1[i+w+1]=="BOOM"):
                b[i]=b[i]+1
        #Ελεγχος για το πρωτο κελι της τελευταιας σειρας
        elif (i==(h*w-w)):
            if (list1[i+1]=="BOOM"):
                b[i]=b[i]+1
            if (list1[i-w]=="BOOM"):
                b[i]=b[i]+1
            if (list1[i-w-1]=="BOOM"):
                b[i]=b[i]+1
                
        #Ελεγχος για το τελευταιο κελι της τελευταιας σειρας
        elif (i==(h*w-1)):
            if (list1[i-1]=="BOOM"):
                b[i]=b[i]+1
            if (list1[i-w]=="BOOM"):
                b[i]=b[i]+1
            if (list1[i-w-1]=="BOOM"):
                b[i]=b[i]+1
                
        #Ελεγχος για την τελευταια σειρα εκτος απο τα ακριανα κελια
        elif (i<(h*w-1) and i>(h*w-w)):
            if (list1[i-1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i+1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-w]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-w+1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-w-1]=="BOOM"):
                 b[i]=b[i]+1
         
        #Ελεγχος της δεξιας στηλης εκτος απο τα ακριανα κελια
        elif ((i+1)%w==0 and i!=0 and i!=(h*w-w)):
            if (list1[i-1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i+w]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i+w-1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-w-1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-w]=="BOOM"):
                 b[i]=b[i]+1
               
        #Ελεγχος της αριστερης στηλης εκτος απο τα ακριανα κελια
        elif ((i%w)==0 and i!=(w-1) and i!=(h*w-1)):
            if (list1[i+1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i+w]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i+w+1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-w+1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-w]=="BOOM"):
                 b[i]=b[i]+1
                
        #Ελεγχος για το εσωτερικο του πινακα
        else :
            if (list1[i+1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i+w]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i+w+1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i+w-1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-w]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-w+1]=="BOOM"):
                 b[i]=b[i]+1
            if (list1[i-w-1]=="BOOM"):
                 b[i]=b[i]+1
                 
                 
for i in range(h*w):                 
    #Tοποθετει τους αριθμους απο τις if στα κελια και οσα εχουν το 0 τα αλλαζε σε κενο
    if (list1[i]=="   "):
        list1[i]=b[i]
    if (list1[i]==0):
        list1[i]="   "  
        
for i in range(h):
    for y in range(w):
        print ("|",list1[i*w+w],"|", end = "")
    print (end="\n")
    
#for i in range (h*w):
#    if ((i+1)%w!=0):
#      print("|  ",list1[i]," | ",end="")
#    else :
#        print("|  ",list1[i]," | ",end="\n")
        
