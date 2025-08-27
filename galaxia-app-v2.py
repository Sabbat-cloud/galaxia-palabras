from flask import Flask, render_template, request, jsonify
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import random
import os
from waitress import serve
import argparse
import sys

# Configuración de NLTK
project_root = os.path.dirname(os.path.abspath(__file__))
nltk_data_path = os.path.join(project_root, 'nltk_data')

# Crear directorio si no existe
os.makedirs(nltk_data_path, exist_ok=True)

# Configurar path de NLTK
nltk.data.path = [nltk_data_path]

# Verificar y descargar recursos si no existen
try:
    word_tokenize("test")
except LookupError:
    print("Descargando recursos de NLTK...")
    nltk.download('punkt', download_dir=nltk_data_path, quiet=True)
    nltk.download('stopwords', download_dir=nltk_data_path, quiet=True)

app = Flask(__name__)

# Variable global para almacenar el texto preprocesado
preprocessed_text = None
preprocessed_word_count = 50

def process_text(text, word_count=50):
    try:
        print(f"Procesando texto de {len(text)} caracteres, mostrando {word_count} palabras")

        # Tokenizar y limpiar texto
        words = word_tokenize(text.lower())
        stop_words = set(stopwords.words('spanish') + stopwords.words('english'))
        words = [word for word in words if word.isalpha() and word not in stop_words]

        print(f"Palabras después de limpiar: {len(words)}")

        # Contar frecuencia de palabras
        word_counts = Counter(words)
        top_words = word_counts.most_common(word_count)

        print(f"Top palabras: {top_words[:5]}") #Debug 

        # Generar datos para visualización 3D
        galaxy_data = []
        for word, count in top_words:
            galaxy_data.append({
                "word": word,
                "count": count,
                "size": min(count * 0.5, 12),
                "x": random.uniform(-50, 50),
                "y": random.uniform(-50, 50),
                "z": random.uniform(-50, 50),
                "color": f"hsl({random.randint(0, 360)}, 100%, 70%)"
            })

        return galaxy_data

    except Exception as e:
        print(f"Error procesando texto: {e}")
        return []

@app.route('/')
def index():
    global preprocessed_text, preprocessed_word_count
    return render_template('index.html', 
                         preprocessed_text=preprocessed_text,
                         preprocessed_word_count=preprocessed_word_count)

@app.route('/process', methods=['POST'])
def process():
    try:
        text = request.form['text']
        word_count = int(request.form.get('word_count', 50))

        print(f"Recibido: word_count={word_count}, text_length={len(text)}")

        if not text.strip():
            return jsonify({"error": "Texto vacío"}), 400

        if word_count < 1 or word_count > 200:
            return jsonify({"error": "El número de palabras debe estar entre 1 y 200"}), 400

        galaxy_data = process_text(text, word_count)

        if not galaxy_data:
            return jsonify({"error": "No se pudieron procesar las palabras"}), 400

        return jsonify(galaxy_data)

    except ValueError:
        return jsonify({"error": "Número de palabras inválido"}), 400
    except Exception as e:
        print(f"Error en endpoint /process: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500

def main():
    global preprocessed_text, preprocessed_word_count
    
    parser = argparse.ArgumentParser(description='Genera una galaxia de palabras a partir de un texto')
    parser.add_argument('archivo', nargs='?', help='Ruta al archivo de texto a procesar')
    parser.add_argument('-n', '--num-palabras', type=int, default=50, 
                       help='Número de palabras a mostrar (por defecto: 50)')
    
    args = parser.parse_args()
    
    # Si se proporciona un archivo, procesarlo
    if args.archivo:
        try:
            with open(args.archivo, 'r', encoding='utf-8') as f:
                preprocessed_text = f.read()
            preprocessed_word_count = args.num_palabras
            print(f"Archivo '{args.archivo}' cargado exitosamente.")
            print(f"Mostrando {preprocessed_word_count} palabras.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            sys.exit(1)
    
    # Iniciar servidor
    host = '0.0.0.0'
    port = 3558
    print(f"Iniciando servidor en http://{host}:{port}")
    print("Presiona Ctrl+C para detener el servidor")
    serve(app, host=host, port=port)

if __name__ == '__main__':
    main()
