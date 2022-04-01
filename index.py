from flask import Flask, render_template, request;
import usuarios

app = Flask(__name__);

@app.route('/', methods=['GET'])
def registro():
    return render_template("index.html");

@app.route('/', methods=['POST'])
def registrar_usuario():
    nombre = request.form['nombre'];
    usuarios.postRegistrarNuevoUsuario(nombre);
    return render_template("usuarios.html");

@app.route('/usuarios', methods=['GET'])
def verUsuarios():
    users = usuarios.getUsuarios();
    list_users = "";
    for i in range(0, len(users)):
        list_users = list_users + users[i] + "\n"

    return render_template("usuarios.html", name = list_users);

if __name__ == '__main__':
    app.run(debug=True, port=3000);