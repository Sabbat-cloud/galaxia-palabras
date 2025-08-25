🌌 Galaxia de Palabras Interactiva
Una aplicación web interactiva que transforma textos en una galaxia 3D de palabras, donde cada planeta representa una palabra y su tamaño corresponde a su frecuencia en el texto.

https://img.shields.io/badge/Visualizaci%C3%B3n-3D%2520Interactiva-blueviolet https://img.shields.io/badge/Tecnolog%C3%ADa-Python%2520%252B%2520Three.js-green https://img.shields.io/badge/Licencia-MIT-lightgrey

✨ Características
Visualización 3D: Representación espacial de palabras como planetas en una galaxia

Procesamiento de texto: Análisis de frecuencia de palabras en español e inglés

Interactividad: Rotación, zoom y selección de elementos

Etiquetas inteligentes: Texto siempre orientado hacia la cámara para mejor legibilidad

Interfaz elegante: Diseño oscuro con efectos visuales atractivos

🛠️ Tecnologías Utilizadas
Backend
Python 3 con Flask

NLTK para procesamiento de lenguaje natural

Tokenización y filtrado de stopwords en español e inglés

Frontend
Three.js para visualización 3D en el navegador

HTML5 y CSS3 con diseño responsive

JavaScript ES6 para la interactividad

📦 Instalación y Uso
Prerrequisitos
Python 3.7 o superior

pip (gestor de paquetes de Python)

Navegador web moderno con soporte para WebGL

Instalación
Clona el repositorio:

bash
git clone https://github.com/Sabbat-cloud/galaxia-palabras.git
cd galaxia-palabras
Crea un entorno virtual y activa:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows
Instala las dependencias:

bash
pip install -r requirements.txt
Descarga los recursos de NLTK (se descargan automáticamente en el primer uso)

Ejecución
Inicia el servidor Flask:

bash
python app-mistral.py
Abre tu navegador y ve a:

text
http://localhost:3558
Pega tu texto, ajusta el número de palabras y haz clic en "🚀 Generar"

🎮 Cómo Usar
Introduce texto: Pega cualquier texto en el área de texto

Configura: Selecciona cuántas palabras quieres visualizar (5-200)

Explora:

Haz clic y arrastra para rotar la galaxia

Usa la rueda del mouse para hacer zoom

Haz clic en cualquier planeta para ver detalles de la palabra

Analiza: Observa las estadísticas de frecuencia y distribución

🏗️ Estructura del Proyecto
text
galaxia-palabras/
├── app-mistral.py          # Servidor Flask principal
├── requirements.txt        # Dependencias de Python
├── nltk_data/             # Recursos de NLP (se crea automáticamente)
├── templates/
│   └── index.html         # Interfaz web completa
└── README.md              # Este archivo
🔧 Personalización
Modificar colores y estilos
Edita las variables CSS en el <style> del archivo index.html para personalizar la apariencia.

Ajustar parámetros 3D
En la función createStar() puedes modificar:

item.size: Tamaño de los planetas

item.x, item.y, item.z: Distribución espacial

Propiedades de materiales y colores

Configurar procesamiento de texto
En app-mistral.py, modifica la función process_text() para:

Cambiar el número máximo de palabras

Ajustar criterios de filtrado

Modificar el algoritmo de distribución

🌟 Ejemplos de Uso
Análisis literario: Visualizar patrones en obras literarias

Estudio de discursos: Analizar frecuencia de palabras en speeches

SEO content: Identificar palabras clave en textos

Educación: Enseñar procesamiento de lenguaje natural de forma visual

🤝 Contribuir
Las contribuciones son bienvenidas. Para contribuir:

Haz fork del proyecto

Crea una rama para tu feature (git checkout -b feature/AmazingFeature)

Commit tus cambios (git commit -m 'Add some AmazingFeature')

Push a la rama (git push origin feature/AmazingFeature)

Abre un Pull Request

📝 Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

🐛 Reportar Problemas
Si encuentras algún problema o tienes sugerencias:

Revisa los issues existentes en GitHub

Crea un nuevo issue con una descripción detallada

Incluye información de tu entorno y pasos para reproducir el problema

📞 Soporte
Si necesitas ayuda o tienes preguntas:

Abre un issue en GitHub

Revisa la documentación de Three.js y Flask

🚀 Roadmap
Exportar visualizaciones como imagen

Modos de color temáticos

Análisis de sentimiento integrado

Comparación entre múltiples textos

Integración con APIs de procesamiento de lenguaje
