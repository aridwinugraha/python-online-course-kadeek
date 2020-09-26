from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    kata = "Coba Flask"
    return render_template('welcome.html', title='Home', string=kata)

@app.route('/profile')
def profile():
    nama = "Ari Dwi Nugraha"
    return render_template('profile.html', title='Profile', string=nama)

if __name__ == '__main__':
    app.run(debug=True)
