import tweepy , oauth

   
Access_token=" "
Access_token_secret=" "
Consumer_key=" "
Consumer_secret=" "
auth = tweepy.OAuthHandler(Consumer_key,Consumer_secret)
auth.set_access_token(Access_token,Access_token_secret)
api=tweepy.API(auth)

u1=input("Give the account of the first user")
u2=input("Give the account of the second user")

userA = tweepy.api.get_user(u1)
userB = tweepy.api.get_user(u2)

folA= userA.followers_count
folB= userB.followers_count

#Παιρνει τα 10 τελευταια tweets απο τον καθε χρηστη
tA = api.GetUserTimeline(screen_name=userA, count=10)
tB = api.GetUserTimeline(screen_name=userB, count=10)

a=[]
b=[]
sumA=0
sumB=0

for i in (tA) :
    #Βαζει ενα ενα τα tweets στην λιστα a
    a.append(i)
    #Κανει split το καθε στοιχειο και το προσθετει στο sum
    sumA = sumA + len(a.split()[i] for j in tA) 
    
    
for k in (tB) :
    #Βαζει ενα ενα τα tweets στην λιστα b
    b.append(k)
    #Κανει split το καθε στοιχειο και το προσθετει στο sum
    sumB = sumB + len(b.split()[k] for j in tB)  
   
    
prA=folA*sumA
prB=folB*sumB
if (prA>prB) :
    print ("The bigger produst belongs to ",userA)
else :
    print ("The bigger product belongs to ",userB)   

    
