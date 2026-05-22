import random
import time
contc = 0
cont = 0
contg = 0
contgc = 0
rngcoin = 1
vant = None
mediat = 0
cont_t = 0
while(cont_t < 100):
    while(contc < 1):
        
        vant = rngcoin
        rngcoin = random.randint(1,2)
        if(rngcoin == vant and rngcoin == 1):
            contc += 1
            contgc += 1
        else:
            contc = 0
        cont+= 1
        contg +=1
        media = contc/cont
        mediat = media + mediat
        
    print(f"{cont_t}contagem de caras:{contc} quantidade total: {cont} ")
    cont_t += 1  
    cont = 0
    contc = 0
    mediag = contgc/contg
    
print(f"{mediag:.5f}%")

    

    


