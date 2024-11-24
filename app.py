from flask import Flask

# Inicializar aplicación Flask
app = Flask(__name__)

# Define ruta raíz o página de inicio
@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/about')
def about():
    return "This is the About page"

# Ejecuta la aplicación en modo depuración para ver errores con detalle
if __name__ == '__main__':
    app.run(debug=True)
