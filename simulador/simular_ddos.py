import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import joblib
import os

# Carrega modelo treinado
modelo_path = os.path.join('detector', 'classificador_treinado.pkl')
modelo = joblib.load(modelo_path)

def simular_pacote():
    # Simula dados de tráfego: tamanho e tempo entre pacotes
    tamanho_pacote = np.random.randint(40, 1500)
    tempo_entre_pacotes = np.random.uniform(0, 1)
    return tamanho_pacote, tempo_entre_pacotes

def analisar_pacote(tamanho, tempo):
    # Usa o modelo para prever se é ataque ou normal
    df = pd.DataFrame([[tamanho, tempo]], columns=['tamanho_pacote', 'tempo_entre_pacotes'])
    pred = modelo.predict(df)[0]
    return 'ATAQUE' if pred == 1 else 'NORMAL'

def alerta_ataques_consecutivos(predicoes, limite=3):
    # Verifica se há ataques consecutivos acima do limite
    count = 0
    for pred in predicoes[::-1]:  # checa do fim para trás
        if pred == 'ATAQUE':
            count += 1
        else:
            break
    if count >= limite:
        print(f"⚠️ Atenção: {count} ataques consecutivos detectados!")

def plotar_resultados(predicoes):
    # Plota gráfico de barras com contagem de ataques e normais
    counts = {'ATAQUE': predicoes.count('ATAQUE'), 'NORMAL': predicoes.count('NORMAL')}
    plt.bar(counts.keys(), counts.values(), color=['red', 'green'])
    plt.title('Contagem de Pacotes Detectados')
    plt.ylabel('Quantidade')
    plt.show()

def main():
    predicoes = []

    print("Iniciando monitoramento simulado. Ctrl+C para parar.")

    try:
        while True:
            tamanho, tempo = simular_pacote()
            pred = analisar_pacote(tamanho, tempo)
            predicoes.append(pred)

            print(f"Pacote: tamanho={tamanho}, tempo={tempo:.3f}s, Predição = {pred}")

            alerta_ataques_consecutivos(predicoes)

            # A cada 20 pacotes, mostrar gráfico
            if len(predicoes) % 20 == 0:
                plotar_resultados(predicoes)

            time.sleep(0.5)  # espera meio segundo entre pacotes

    except KeyboardInterrupt:
        print("\nMonitoramento finalizado pelo usuário.")
        plotar_resultados(predicoes)

if __name__ == '__main__':
    main()




