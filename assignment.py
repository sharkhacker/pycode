test= int(input())
for t in range(0, test):
    a=str(input())
    b=str(input())
    lin=0
    cir=0
    for i in range(len(a)):
        	lin+=abs(ord(a[i])-ord(b[i]))
        
    for j in range(len(a)):
         cir1=abs(ord(a[j])-ord(b[j]))
         x=ord(a[j])
         y=ord(b[j])
         mi=min(x,y)
         ma=max(x,y)
         cir1=ma-mi
         cir2=abs((26-ma)+(mi))
         cir+=min(cir1,cir2)
        	  
        
    print("answer :",lin,cir)
    


