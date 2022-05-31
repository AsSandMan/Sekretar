import random
zzz=[]
for i in range(256):
    for j in range(256):
        for k in range(256):
            zzz.append([i,j,k])
            
print(random.sample(zzz, 5)) 
