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
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        total_rooms = int(request.form['total_rooms'])
        total_bedrooms = int(request.form['total_bedrooms'])
        ocean_proximity = int(request.form['ocean_proximity'])

        
        # Crear la matriz de entrada para la predicción
        input_features = np.array([[latitude, longitude, total_rooms, total_bedrooms, ocean_proximity]])
        
        # Hacer la predicción
        prediction = model.predict(input_features)[0]
        
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
