import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

def treinar_modelo():
    print("Lendo o arquivo CSV...")
    import pandas as pd
    dados = pd.read_csv('data/trafego_simulado.csv')
    print("Colunas encontradas no CSV:", dados.columns)
    print(f"Dados lidos: {dados.shape[0]} linhas, {dados.shape[1]} colunas")

    X = dados[['tamanho_pacote', 'tempo_entre_pacotes']]
    y = dados['ataque']

    print("Separando dados de treino e teste...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Treinando o modelo...")
    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)

    print("Fazendo previsões no conjunto de teste...")
    y_pred = modelo.predict(X_test)

    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("Relatório de classificação:\n", classification_report(y_test, y_pred))

    # SALVAR o modelo treinado em um arquivo .pkl
    caminho_modelo = os.path.join(os.path.dirname(__file__), "classificador_treinado.pkl")
    joblib.dump(modelo, caminho_modelo)
    print(f"Modelo salvo em {caminho_modelo}")

    return modelo

# Só treina se rodar diretamente este arquivo
if __name__ == '__main__':
    treinar_modelo()
