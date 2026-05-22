vi = int(input("Digite o valor inicial da sequencia de fibonnati: "))
n = int(input("Quantos termos quer gerar:"))
n = n - 1
t = 0
va = vi
ava = 0
print(vi)
for t in range(n):
    
    vat = ava+ va
    vatf = f"{vat:,}".replace(",", ".")
    ava = va
    va = vat
    print(vatf)
    
