import random
import time
from collections import Counter

# ESTA É A ÚnICA LINHA QUE CONTROLA A QUANTIDADE DE SIMULAÇÕES:
NUM_SIMULACOES = 1000# Altere este número para mudar a quantidade

# Exemplos de como modificar e tempos estimados (em máquina comum, aprox.):
# NUM_SIMULACOES = 1000      # Tempo: < 1 segundo
# NUM_SIMULACOES = 10000     # Tempo: 1-3 segundos
# NUM_SIMULACOES = 1000000   # Tempo: 20-60 segundos
# NUM_SIMULACOES = 1000000000 # 1 bilhão: Horas ou dias (otimize com multiprocessing)

# Times da Copa 2026 (simplificado com 16 principais, potências de fogo)
times = [
    'Brasil', 'Argentina', 'França', 'Espanha', 'Inglaterra', 'Alemanha',
    'Portugal', 'Holanda', 'Itália', 'Uruguai', 'Bélgica', 'Croácia',
    'México', 'EUA', 'Canadá', 'Japão'
]

# Forças relativas (0-100, baseadas em ranking FIFA aproximado)
forcas = {
    'Brasil': 92, 'Argentina': 90, 'França': 89, 'Espanha': 88,
    'Inglaterra': 87, 'Alemanha': 86, 'Portugal': 85, 'Holanda': 84,
    'Itália': 83, 'Uruguai': 82, 'Bélgica': 81, 'Croácia': 80,
    'México': 78, 'EUA': 76, 'Canadá': 75, 'Japão': 74
}

def prob_vitoria(time1, time2):
    f1 = forcas[time1]
    f2 = forcas[time2]
    return f1 / (f1 + f2)

def simular_partida(time1, time2):
    if random.random() < prob_vitoria(time1, time2):
        return time1
    return time2

def simular_torneio(times):
    competidores = list(times)
    while len(competidores) > 1:
        random.shuffle(competidores)
        nova_rodada = []
        i = 0
        while i < len(competidores):
            if i + 1 < len(competidores):
                vencedor = simular_partida(competidores[i], competidores[i + 1])
                nova_rodada.append(vencedor)
                i += 2
            else:
                nova_rodada.append(competidores[i])
                i += 1
        competidores = nova_rodada
    return competidores[0]

print(f"Iniciando {NUM_SIMULACOES:,} simulações da Copa 2026...")
inicio = time.time()
vencedores = [simular_torneio(times) for _ in range(NUM_SIMULACOES)]
fim = time.time()

contagem = Counter(vencedores)
total = len(vencedores)
print("\nProbabilidades de vitória (%):")
for time, count in contagem.most_common():
    pct = (count / total) * 100
    print(f"{time}: {pct:.2f}% ({count:,})")
print(f"\nTempo total: {fim - inicio:.2f} segundos")
print(f"Média por simulação: {(fim - inicio)/NUM_SIMULACOES*1000:.2f} ms")