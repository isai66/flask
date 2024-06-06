from flask import Flask, request, send_from_directory, render_template_string
import os

app = Flask(__name__)
EDAD_REAL = 21

@app.route('/', methods=['GET', 'POST'])
def home():
    # Use render_template_string to embed HTML directly
    message = None
    if request.method == 'POST':
        try:
            age = int(request.form.get('age'))
            if age == EDAD_REAL:
                message = "¡Acertaste! Tengo 21 años (Aunque en esta foto tengo 17 😬)"
            else:
                message = "Fallaste. Inténtalo de nuevo."
        except ValueError:
            message = "Por favor, ingresa un número válido."

    return render_template_string('''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Hola Mundo</title>
      </head>
      <body>
        <center>
        <h1>Hola Mundo</h1>
        <h2>Soy Isaí Lara Mojica, con matricula 20211065 del Grupo B</h2>
        <img src="{{ url_for('get_image', filename='avatar.png') }}" alt="My Image" style="width: 200px;">
        <form method="POST">
          <label for="age">Adivina mi edad:</label>
          <input type="number" id="age" name="age">
          <input type="submit" value="Enviar">
        </form>
        {% if message %}
          <p>{{ message }}</p>
        {% endif %}
        </center>
      </body>
    </html>
    ''', message=message)

@app.route('/image/<filename>')
def get_image(filename):
    # Return the image from the same directory
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), filename)

if __name__ == '__main__':
    app.run(debug=True)
