import pandas as pd

from Constantes import Constantes


class CSVHandler:

    @staticmethod
    def ler_csv(caminho_arquivo):
        return pd.read_csv(caminho_arquivo)

    @staticmethod
    def remover_nomes(df, nomes_remover):
        # Remove as linhas que contêm os nomes indicados
        df = df[~df[Constantes.COLUNA_NOME_COMPLETO].isin(nomes_remover)]
        # Verifica se algum nome da lista 'nomes_remover' está no DataFrame filtrado
        for nome in nomes_remover:
            if nome in df[Constantes.COLUNA_NOME_COMPLETO].values:
                print(f"Erro: {nome} ainda está no DataFrame após a exclusão.")
                return df
        print("Todos os nomes foram removidos com sucesso.")
        return df
