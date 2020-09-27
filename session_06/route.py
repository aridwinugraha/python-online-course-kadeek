from flask import Flask, request
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

@app.route('/input')
def input():
    return render_template('input.html', title='Input')

@app.route('/actInput', methods=["POST"])
def actInput():
    nama = request.form.get('nama')
    return render_template('hasil.html', title='Home', nama=nama)

@app.route('/hasil/<angka>')
def hasil(angka):
    angka = angka
    return render_template('hasil.html', title='Home', angka=angka)

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/beranda', methods=["POST"])
def beranda():
    user = str(request.form.get('user'))
    password = str(request.form.get('password'))

    if (user == "Ari Dwi Nugraha" and password == "123"):
        return render_template('beranda.html', title='Beranda', user=user)
    else:
        return render_template('gagal.html', title='Error')

if __name__ == '__main__':
    app.run(debug=True)
