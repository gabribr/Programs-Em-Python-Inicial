import random
cont = 0
contc1 = 0
contc2 = 0
contc3 = 0
contc4 = 0
contc5 = 0
contca1 = 0
contca2= 0
contca3= 0
contca4= 0
contca5= 0
conte1= 0
conte2 = 0
conte3 = 0
conte4 = 0
conte5 = 0
nomec = ""
nomeca = ""
nomee = ""
while(cont<1000):
    casamento = random.randint(1,5)
    match casamento:
        case 1:
            contc1 += 1
        case 2:
            contc2+= 1
        case 3:
            contc3 += 1
        case 4:
            contc4 +=1
        case 5:
            contc5 +=1
    casa = random.randint(1,5)
    match casa:
        case 1:
            contca1+= 1
        case 2:
            contca2+= 1
        case 3:
            contca3 += 1
        case 4:
            contca4+=1
        case 5:
            contca5+=1
    emprego = random.randint(1,5)
    match emprego:
        case 1:
            conte1+= 1
        case 2:
            conte2+= 1
        case 3:
            conte3 += 1
        case 4:
            conte4+=1
        case 5:
            conte5+=1
    cont+= 1
variaveisc = {
    "1": contc1,
    "2": contc2,
    "3": contc3,
    "4": contc4,
    "5": contc5
}
variaveisca = {
    "1": contca1,
    "2": contca2,
    "3": contca3,
    "4": contca4,
    "5": contca5
}
variaveise = {
    "1": conte1,
    "2": conte2,
    "3": conte3,
    "4": conte4,
    "5": conte5
}
nome_da_maiorc = max(variaveisc, key=variaveisc.get)
nome_da_maiorca = max(variaveisca, key=variaveisca.get)
nome_da_maiore = max(variaveise, key=variaveise.get)
valor_da_maiorc = variaveisc[nome_da_maiorc]
valor_da_maiorca= variaveisca[nome_da_maiorca]
valor_da_maiore = variaveise[nome_da_maiore]
pc = valor_da_maiorc/cont*100
pca = valor_da_maiorca/cont*100
pe = valor_da_maiore/cont*100
match nome_da_maiore:
        case "1":
            nomee = "Programador"
        case "2":
            nomee = "Empresario"
        case "3":
            nomee = "Vendedor"
        case "4":
            nomee = "Zelador"
        case "5":
            nomee = "Mendigo"
match nome_da_maiorc:
        case "1":
            nomec = "Duda"
        case "2":
            nomec = "Carolina"
        case "3":
            nomec = "Catarina"
        case "4":
            nomec = "Paula"
        case "5":
            nomec = "Ninguem"
match nome_da_maiorca:
        case "1":
            nomeca = "Casa"
        case "2":
            nomeca = "Apartamento"
        case "3":
            nomeca = "Estudio"
        case "4":
            nomeca = "Barracão"
        case "5":
            nomeca = "Rua"
print("Casa",nomeca , "porcentagem :", pca)
print("Mulher", nomec , "porcentagem :",pc)
print("Emprego", nomee ,"porcentagem :",pe)


    
       
    