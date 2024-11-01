from Constantes import Constantes


class Acessos:
    def __init__(self, df, contexto, componente, nome_evento):
        self.df = df
        self.contexto = contexto
        self.componente = componente
        self.nome_evento = nome_evento

    def filtra_videos(self):
        return self.df[
            (self.df[Constantes.COLUNA_CONTEXTO_EVENTO].str.contains(self.contexto)) &
            (self.df[Constantes.COLUNA_COMPONENTE] == self.componente) &
            (self.df[Constantes.COLUNA_NOME_EVENTO] == self.nome_evento)
            ]

    @staticmethod
    def conta_acessos_unicos(df_videos):
        grupo_videos = df_videos.groupby([Constantes.COLUNA_CONTEXTO_EVENTO])
        acessos_unicos = grupo_videos[Constantes.COLUNA_NOME_COMPLETO].nunique()
        df_acessos_unicos = acessos_unicos.reset_index(name='Acessos únicos por vídeo')
        return df_acessos_unicos
