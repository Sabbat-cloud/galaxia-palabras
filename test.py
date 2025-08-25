import nltk
import os

project_root = os.path.dirname(os.path.abspath(__file__))
nltk_data_path = os.path.join(project_root, 'nltk_data')

os.makedirs(nltk_data_path, exist_ok=True)
nltk.data.path = [nltk_data_path]

# Descargar recursos
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)

# Probar tokenización
from nltk.tokenize import word_tokenize
text = "Hola mundo esto es una prueba"
print("Tokenización:", word_tokenize(text))
