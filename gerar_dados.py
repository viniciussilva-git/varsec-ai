import random
import csv

def gerar_trafego_normal(n):
    dados = []
    for _ in range(n):
        # tráfego normal: pacotes com tamanho entre 40 e 150 bytes
        tamanho = random.randint(40, 150)
        tempo = random.uniform(0.05, 0.5)  # tempo entre pacotes em segundos
        dados.append([tamanho, tempo, 0])  # 0 = normal
    return dados

def gerar_trafego_ddos(n):
    dados = []
    for _ in range(n):
        # tráfego DDoS: pacotes grandes, enviados muito rápido
        tamanho = random.randint(1000, 1500)
        tempo = random.uniform(0.001, 0.01)
        dados.append([tamanho, tempo, 1])  # 1 = ataque
    return dados

def salvar_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(['tamanho_pacote', 'tempo_entre_pacotes', 'ataque'])  # cabeçalho
        writer.writerows(dados)

if __name__ == '__main__':
    normal = gerar_trafego_normal(1000)
    ddos = gerar_trafego_ddos(200)
    todos_dados = normal + ddos
    salvar_csv('data/trafego_simulado.csv', todos_dados)
    print("✅ Arquivo 'trafego_simulado.csv' criado em data/")

