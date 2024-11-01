import ipywidgets as widgets
import pandas as pd
from IPython.display import display

from Acessos import Acessos
from Grafico import Grafico


class ArquivoUpload:
    def __init__(self):
        self.carregador_arquivo = widgets.FileUpload(accept='.csv', multiple=False)
        self.botao_carregar = widgets.Button(description="Carregar CSV")
        self.botao_gerar_grafico = widgets.Button(description="Gerar Gráfico de Barras")
        self.saida = widgets.Output()

        # Campos de texto para os parâmetros de filtragem
        self.campo_contexto = widgets.Text(description="Contexto:")
        self.campo_componente = widgets.Text(description="Componente:")
        self.campo_nome_evento = widgets.Text(description="Nome Evento:")

        # Evento para o botão de upload
        self.botao_carregar.on_click(self.ao_carregar_arquivo)
        # Evento para o botão de gerar gráfico
        self.botao_gerar_grafico.on_click(self.ao_gerar_grafico)

        # DataFrame vazio para ser usado na análise
        self.df = None

    def ao_carregar_arquivo(self, b):
        with self.saida:
            self.saida.clear_output()  # Limpa a saída anterior
            if self.carregador_arquivo.value:
                for nome_arquivo, arquivo_info in self.carregador_arquivo.value.items():
                    try:
                        # Carrega os dados do CSV em um DataFrame
                        self.df = pd.read_csv(arquivo_info['content'])
                        print(f"Arquivo {nome_arquivo} carregado com sucesso!")
                    except Exception as e:
                        print(f"Erro ao carregar o arquivo: {e}")
            else:
                print("Nenhum arquivo foi selecionado.")

    def ao_gerar_grafico(self, b):
        if not hasattr(self, 'df') or self.df is None:
            print("O arquivo não foi carregado corretamente.")
            return

        with self.saida:
            self.saida.clear_output()
            if self.df is not None:
                # Realiza a filtragem e contagem de acessos únicos
                contexto = self.campo_contexto.value
                componente = self.campo_componente.value
                nome_evento = self.campo_nome_evento.value

                acessos = Acessos(self.df, contexto, componente, nome_evento)
                df_videos_filtrados = acessos.filtra_videos()
                df_acessos_unicos = Acessos.conta_acessos_unicos(df_videos_filtrados)

                # Gera o gráfico usando a classe Grafico
                grafico = Grafico(df_acessos_unicos)
                grafico.plota_barras(contexto)
            else:
                print("Por favor, faça o upload de um arquivo CSV primeiro.")

    def exibir(self):
        # Exibe os widgets
        display(self.carregador_arquivo, self.botao_carregar)
        display(self.campo_contexto, self.campo_componente, self.campo_nome_evento, self.botao_gerar_grafico,
                self.saida)
