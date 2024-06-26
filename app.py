from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Cargar el modelo
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        latitud = float(request.form['latitud'])
        longitud = float(request.form['longitud'])
        num_cuartos = int(request.form['num_cuartos'])
        num_habitaciones = int(request.form['num_habitaciones'])
        
        # Crear la matriz de entrada para la predicción
        input_features = np.array([[latitud, longitud, num_cuartos, num_habitaciones]])
        
        # Hacer la predicción
        prediction = model.predict(input_features)[0]
        
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
