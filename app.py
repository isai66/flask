from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    genre = None
    if request.method == 'POST':
        liveness = float(request.form['liveness'])
        instrumentalness = float(request.form['instrumentalness'])
        vocalness = float(request.form['vocalness'])
        
        # Lógica para determinar el género
        if instrumentalness > 7:
            genre = 'Instrumental'
        elif vocalness > 7:
            genre = 'Pop'
        elif liveness > 7:
            genre = 'Rock'
        else:
            genre = 'Clásica'

    return render_template('index.html', genre=genre)

if __name__ == '__main__':
    app.run(debug=True)
