from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def obtener_productos():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    
    if response.status_code == 200:
        productos = response.json()
        return render_template('index.html', productos=productos)
    else:
        return "Error al obtener los productos", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)