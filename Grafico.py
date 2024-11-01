from matplotlib import pyplot as plt

from Constantes import Constantes


class Grafico:
    def __init__(self, df_acessos_unicos):
        self.df_acessos_unicos = df_acessos_unicos

    # Configura o gráfico com título, rótulos e limites
    def configura_grafico(self, ax, contexto, nome_coluna):
        # Tìtulo
        ax.set_title(f'{contexto}: {nome_coluna}')

        # Estabelece o limite superior dinâmico do eixo y (conforme o valor máximo)
        max_acessos = self.df_acessos_unicos[Constantes.COLUNA_ACESSOS_UNICOS].max()
        ax.set_ylim(0, max_acessos + 10)

        # Rótulos
        ax.set_xlabel('Vídeos')
        ax.set_ylabel('Número de Acessos Únicos')
        ax.tick_params(axis='x', rotation=45)
        plt.xticks(ha='right')

        # Linhas de referência (grid) na horizontal
        ax.grid(axis='y', zorder=0)

    # Adiciona os rótulos de valores acima das barras
    def adiciona_rotulos(self, ax):
        for i, valor in enumerate(self.df_acessos_unicos[Constantes.COLUNA_ACESSOS_UNICOS]):
            ax.text(i, valor + 0.1, str(valor), ha='center', va='bottom', zorder=4)

    def formata_rotulo(self):
        self.df_acessos_unicos[Constantes.COLUNA_NOME_LIMPO] = \
            (self.df_acessos_unicos[Constantes.COLUNA_CONTEXTO_EVENTO].str.replace
             ('Conteúdo Interativo H5P:', '', regex=False).str.strip())

    # Plota um gráfico de barras
    def plota_barras(self, contexto):
        self.formata_rotulo()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(self.df_acessos_unicos[Constantes.COLUNA_NOME_LIMPO],
               self.df_acessos_unicos[Constantes.COLUNA_ACESSOS_UNICOS], zorder=3)
        nome_coluna = self.df_acessos_unicos.columns[1]
        self.configura_grafico(ax, contexto, nome_coluna)
        self.adiciona_rotulos(ax)
        plt.tight_layout()
        plt.show()
