import nltk
import os

# Configurar paths
project_root = os.path.dirname(os.path.abspath(__file__))
nltk_data_path = os.path.join(project_root, 'nltk_data')

# Crear directorio
os.makedirs(nltk_data_path, exist_ok=True)

# Descargar recursos
print("Descargando recursos de NLTK...")
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)
nltk.download('punkt_tab', download_dir=nltk_data_path)
print("Recursos descargados correctamente!")
