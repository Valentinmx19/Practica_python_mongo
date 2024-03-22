from faker import Faker
from logica import UsuarioDAO

# Crea documentos usando los metodos de faker, en este archivo tienes ya disponible faker
# pudes llamar a los siguientes metodos que nos da el modulo de faker:
#       first_name(), last_name(), random_int(min=1980, max=2000), state()

# ejemplo (solo para que vean como juncia):

fake = Faker()

user = UsuarioDAO()

usuario = {
    'nombre': fake.first_name(),
    'apellido_paterno': fake.last_name(),
    'apellido_materno': fake.last_name(),
    'año_de_nacimiento': fake.random_int(min=1980, max=2020),
    'edad': fake.random_int(min=1, max=99),
    'estado': fake.state(),
    'correo': fake.email(),
    'clave_secreta': ''
}

##DESCOMENTAR LO NECESARIO!!

# 1 Probar CRUD

# user.agregar_usuario(usuario)
# user.actualizar_usuario(2, {"nombre": "Pedro"})
# print(user.obtener_usuario_por_id(2))
# user.eliminar_usuario(2)
# print(user.obtener_usuario_por_id(2))


## 3 Utilizando `faker` y estructuras cíclicas:

# for i in range(0, 10):
#     usuario = {
#         'nombre': fake.first_name(),
#         'apellido_paterno': fake.last_name(),
#         'apellido_materno': fake.last_name(),
#         'año_de_nacimiento': fake.random_int(min=1980, max=2020),
#         'edad': fake.random_int(min=1, max=99),
#         'estado': fake.state(),
#         'correo': fake.email(),
#         'clave_secreta': ''
#     }
#     user.agregar_usuario(usuario)

# cont = 0
# while cont < 7:
#     usuario = {
#         'nombre': fake.first_name(),
#         'apellido_paterno': fake.last_name(),
#         'apellido_materno': fake.last_name(),
#         'año_de_nacimiento': fake.random_int(min=1980, max=2020),
#         'edad': fake.random_int(min=1, max=99),
#         'estado': fake.state(),
#         'correo': fake.email(),
#         'clave_secreta': ''
#     }
#     user.agregar_usuario(usuario)
#     cont += 1

# countUsers = 0
# for uuser in user.obtener_usuarios():
#     countUsers += 1


# for i in range(0, countUsers):
#     usuario = {
#         'nombre': fake.first_name(),
#         'apellido_paterno': fake.last_name(),
#         'apellido_materno': fake.last_name(),
#         'año_de_nacimiento': fake.random_int(min=1980, max=2020),
#         'edad': fake.random_int(min=18, max=99),
#         'estado': fake.state(),
#         'correo': fake.email(),
#         'clave_secreta': ''
#     }
#     user.agregar_usuario(usuario)


##4. Con código Python, muestra todos los usuarios de la coleccion que son mayores de 7 años y menores de 25.

# greatThan7lowtThan25 = [uuser for uuser in user.obtener_usuarios() if (uuser.get("edad") > 7 and uuser.get("edad") < 25)]

##5. Muestra por consola al primer usuario de menor edad de la colección.

# for uuser in user.obtener_usuarios():
#     if uuser.get("edad") < 18:
#         print(uuser)
#         break

##6. Muestra por consola al primer usuario de mayor edad de la colección.

# for uuser in user.obtener_usuarios():
#     if uuser.get("edad") >= 18:
#         print(uuser)
#         break

##7. Muestra por consola únicamente los nombres de todos los documentos de la colección.

# names = [uuser.get("nombre") for uuser in user.obtener_usuarios()]
# print(names)

# 8. Crea una función que genere una clave secreta para cada usuario a partir de su información. La clave debe contener:
#    - Dos primeras letras de su nombre.
#    - Primera letra de apellido materno.
#    - Primeras dos letras de su apellido paterno.
#    - Últimos dos dígitos de su fecha de nacimiento.
#    - Edad.
#    - Primera y últimas dos letras de su estado.
#    - Todos los caracteres que se encuentran antes del '@' en su correo electrónico.

def ultimos_dos__digitos(nombre):
    name = str(nombre)
    data = ''
    nam = len(name) - 2
    while nam < len(name): 
        data += name[nam]
        nam += 1
    return data 

def clave_secreta(nombre, apellido_mat, apellido_pat, fecha_nac, edad, estado, email):
    name = nombre[0:2]
    lastname = apellido_mat[0]
    lastname_two = apellido_pat[0:2]
    date = ultimos_dos__digitos(fecha_nac)
    estate = f'{estado[0]}{ultimos_dos__digitos(estado)}'
    mail = ''
    for i in email:
        if i == '@':
            break
        mail += i

    return f'{name}{lastname}{lastname_two}{date}{edad}{estate}{mail}'

for uuser in user.obtener_usuarios():
    if uuser.get("id") < 5: 
        ide = uuser.get("id")
        name = uuser.get("nombre")
        apm = uuser.get("apellido_materno")
        app = uuser.get("apellido_paterno")
        date = uuser.get("año_de_nacimiento")
        age = uuser.get("edad")
        state = uuser.get("estado")
        email = uuser.get("correo")

        clave = clave_secreta(name, apm, app, date, age, state, email)

        user.actualizar_usuario(ide, {"clave_secreta": clave})

for uus in user.obtener_usuarios():
    if uus.get("id") < 5: 
        print(uus)

