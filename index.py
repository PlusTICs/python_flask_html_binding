from flask import Flask, render_template, request;
import usuarios

app = Flask(__name__);

@app.route('/', methods=['GET'])
def vista_login():
    return render_template("login.html");

@app.route('/', methods=['POST'])
def login():
    user = request.form['usuario'];
    paswd = request.form['contrasenia'];
    if(usuarios.loginSuperUser(user, paswd) == True):
        return render_template("usuarios.html", name = usuarios.getUsuarios());
    else:
        return render_template("login.html");

@app.route('/usuarios', methods=['GET'])
def vista_registro_usuario():
    return render_template("index.html");

@app.route('/usuarios', methods=['POST'])
def registrar_usuario():
    nombre = request.form['nombre'];
    usuarios.postRegistrarNuevoUsuario(nombre);
    return render_template('usuarios.html', name = usuarios.getUsuarios());

if __name__ == '__main__':
    app.run(debug=True, port=3000);