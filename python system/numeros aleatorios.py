import random
contt = 0
n = 0
sair = True
pergunta = 0
while sair:
    while contt < 5:
        if contt == 0:
            n = random.randint(1,100)
        num = int(input("\n\n\nDigite um Numero:"))
        if num == n:
            print("\n\nvocê acertou\n\n Seu numero de tentativas foi - ",contt)
            contt = 6
        else:
            contt += 1
            print("\n\ntente novamente\n\n você tem mais -    ",5 - contt,"  tentativas" )
            if num < n:
                print("\n\n seu numero e maior")
            else:
                print("\n\nseu numero e menor")
    print("\nseu numero era - ",n)
    print("\n\n1-sim\n2-não")
    pergunta = int(input("\nVocê quer sair:"))
    if pergunta == 1:
        sair = False
    else:
        pergunta = True
        contt = 0
