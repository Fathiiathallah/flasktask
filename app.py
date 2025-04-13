from flask import Flask, render_template

app = Flask(__name__)


# First route di flask "hello world"
@app.route("/")
def hello_world():
    return "<p>Hello, Apakabar!</p>"



# Second route di flask
@app.route("/aplikasi/")
def aplikasi():
    return "<p>Ini adalah aplikasi flask pertama saya!</p>"


# Third route dengan HTML
@app.route("/about/")
def about():
    return render_template('about_without_boostrap.html')

# Fourth route dengan HTML dan Bootstrap
@app.route("/about-bootstrap/")
def about_bootstrap():
    return render_template('about_with_boostrap.html')  


# Fifth route Dinamis
@app.route('/nama/<string:nama_mahasiswa>/')
def getnama(nama_mahasiswa):
    return "nama anda adalah {}".format(nama_mahasiswa)



# Sixth.1 route 
app = Flask(__name__)
@app.route('/user/<name>/')  # Variabel name diambil dari URL
def user(name):
    return f"Hello, {name}!"


# Sixth.2 route ID
@app.route('/user/<int:user_id>/')  # Hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"



# Sixth.3 route dengan Template HTML
app = Flask(__name__)
@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', username=name)


# Sixth.4 route Variable Global
app_name = "My Thys Flask App"  # Variabel global

@app.route('/variable-global/')
def variable_global():
    return f"Welcome to {app_name}!"


# Sixth.5 route dengan dictonary
@app.route('/data/')
def data():
    user = {"name": "Thy", "age": 20, "city": "Makassar"}
    return render_template('data.html', user=user)


# Seventh route FOR dan IF Statement
# Seventh.1 Statement dalam Template Flask
@app.route('/users/')
def users():
    user_list = ["Thy", "Kemal", "Arun", "Dwi"]
    return render_template('users.html', users=user_list)


# Seventh.2 for dan if dalam Satu Loop
@app.route('/users/')
def users():
    user_list = [
        {"name": "Thy", "role": "admin"},
        {"name": "Kemal", "role": "user"},
        {"name": "Arun", "role": "admin"},
        {"name": "Dwi", "role": "user"},
    ]
    return render_template('users.html', users=user_list)



# Eighth route If Elif and Else
# Eighth.1 if, elif, dan else dalam Template Flask
@app.route('/nilai/<int:score>/')
def nilai(score):
    return render_template('nilai.html', score=score)


# Eighth.2 route for dengan if-elif-else
@app.route('/mahasiswa/')
def mahasiswa():
    daftar_mahasiswa = [
        {"nama": "Thy", "nilai": 92},
        {"nama": "Kemal", "nilai": 80},
        {"nama": "Arun", "nilai": 65},
        {"nama": "Dwi", "nilai": 55},
    ]
    return render_template('mahasiswa.html', mahasiswa=daftar_mahasiswa)


if __name__ == "__main__":
    app.run()
