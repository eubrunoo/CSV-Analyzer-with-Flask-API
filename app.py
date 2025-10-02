from libs import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/files', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"erro": "Nenhum campo de arquivo na requisição."})
    
    archive = request.files['file']

    if archive.filename == '':
        return jsonify({"erro": "Nenhum arquivo selecionado."})

    if archive and archive.filename.endswith('.csv'):

        file_id = str(uuid.uuid4())

        new_filename = f"{file_id}.csv"

        destination_path = os.path.join('uploads', new_filename)

        archive.save(destination_path)

        return jsonify({
                "message": "Arquivo enviado com sucesso!",
                "file_id": file_id
            })
    else:
        return jsonify({"erro": "Formato de arquivo inválido. Por favor, envie um .csv."})
    
@app.route('/files/<file_id>/analysis', methods=['POST'])
def analyse_file(file_id):
    filepath = os.path.join('uploads', f"{file_id}.csv")

    if not os.path.exists(filepath):
        return jsonify({"erro": "Arquivo com este ID não encontrado."}), 404

    try:
        col_produto = request.form['coluna_produto']
        col_preco = request.form['coluna_preco']
        col_qtd = request.form['coluna_quantidade']
        col_cliente = request.form['coluna_cliente']

        dataframe = pd.read_csv(filepath)

        resultado_analise = processar_dados_vendas(
            dataframe, 
            col_produto,
            col_preco,
            col_qtd,
            col_cliente
        )

        return jsonify(resultado_analise)
    
    except KeyError as e:
        return jsonify({"erro": f"A coluna '{str(e)}' informada não foi encontrada no arquivo CSV."}), 400
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro inesperado: {str(e)}"}), 500