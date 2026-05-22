ninicial = float(input("Valor Inicial da PA: "))
n = 0
vt = 0
print("R$",ninicial)
for n in range(27):
    ninicial = ninicial*2
    vt = vt + ninicial
    print("R$",ninicial)
numero_formatado = f"{vt:,}".replace(",", ".")
print("R$",numero_formatado)