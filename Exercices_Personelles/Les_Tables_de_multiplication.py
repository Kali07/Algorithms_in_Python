#20 premiers termes de multiplication

#fontion table de multiplication de n

def table(n) :
    for i in range(1,13):
        print(i,"x",n,"=",i*n)

#fonction maximum
        
def maximum(a,b,c):
    maxim = a
    if a <= b and b >= c:
        maxim = b
    elif b <= c and a <= c :
        maxim = c
    print("le maximum est ",maxim)

#conversion temperature
"""
for i in range(1,21) :
    print(i,"x","53 =",i*53)
    #print('{:4d}'.format(i))
    
#12 premiers table de multiplication

for i in range(2,13) :
    for j in range (1,13):
        print(i,"x",j,"=",i*j)
"""
#table(2)
maximum(6000,820,1244)

