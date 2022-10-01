

usuario=input("ingresa tu nombre de usuario: ")

def devuelve_usuario(n1):
    if len(n1)<5:
        return "el usuario debe ser mayor a 5 caracteres"
    elif len(n1)>15:
        return "el usuario debe ser menor a 15 caracteres"
    elif usuario.isalnum():
        return usuario.isalnum()

print(devuelve_usuario(usuario))


    
