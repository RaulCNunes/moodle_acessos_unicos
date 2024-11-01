from flask import Flask, request, render_template, jsonify
from CSVHandler import CSVHandler
from Acessos import Acessos
from Grafico import Grafico
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # pasta onde arquivos CSV serão armazenados

# conferir se a pasta 'uploads' existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Receber o arquivo CSV
        if 'file' not in request.files:
            return jsonify({"error": "Nenhum arquivo encontrado."}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Nenhum arquivo selecionado."}), 400
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Receber os parâmetros do formulário
        contexto = request.form.get("contexto", "")
        componente = request.form.get("componente", "")
        nome_evento = request.form.get("nome_evento", "")

        # Lê o arquivo CSV
        df_log = CSVHandler.ler_csv(file_path)

        # Realiza a filtragem e conta os acessos únicos
        acessos = Acessos(df_log, contexto, componente, nome_evento)
        df_videos = acessos.filtra_videos()
        df_acessos_unicos = acessos.conta_acessos_unicos(df_videos)

        # Gera o gráfico de barras e retorna uma mensagem de sucesso
        grafico = Grafico(df_acessos_unicos)
        grafico.plota_barras(contexto)  # O gráfico pode ser salvo como imagem

        return jsonify({"message": "Arquivo processado e gráfico gerado com sucesso!"})

    return render_template("index.html")  # Renderiza o formulário para upload


if __name__ == "__main__":
    app.run(debug=True)
