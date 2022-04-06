usuarios = ["Ervin", "Andres"];

usuario = 'Andres';
pasword = 'andres123';

def getUsuarios():
    return usuarios;

def postRegistrarNuevoUsuario(nombre):
    usuarios.append(nombre);

def loginSuperUser(user, paswd):
    login = False;
    if(user == usuario and paswd == pasword):
        login = True
    return login;