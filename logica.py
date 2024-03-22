# Implementa la lógica para las operaciones CRUD que faltan en esta clase,
# utilizando los métodos disponibles en self.collection:

# - insertOne(): Agrega un nuevo usuario a la colección.

# - find(): Recupera todos los usuarios de la colección.

# - find_one(): Recupera un usuario específico mediante un objeto de MongoDB
#   con la clave 'id' y el valor del id del usuario, por ejemplo, {'id': usuario_id}.

# - update_one(): Actualiza un usuario específico utilizando su 'id' y
#   aplicando los nuevos datos proporcionados.

# - delete_one(): Elimina un usuario específico según su 'id'.

from conexion import ConexionMongo


class UsuarioDAO:
    def __init__(self):
        self.conexion = ConexionMongo()
        self.collection = self.conexion.db['usuarios']

        self.max_id = self.get_max_id()

    def get_max_id(self):
        max_id = self.collection.find_one({}, sort=[("id", -1)])
        return max_id.get('id', 0) if max_id else 0

    def agregar_usuario(self, usuario):
        self.max_id += 1
        usuario['id'] = self.max_id
        self.collection.insert_one(usuario)

    def obtener_usuarios(self):
        return self.collection.find()

    def obtener_usuario_por_id(self, idUser):
        try:
            user = self.collection.find_one({'id': idUser})
            return user
        except: return 'Proporcione un dato válido'

    def actualizar_usuario(self, data_update, data):
        self.collection.update_one({'id': data_update}, {'$set': data})

    def eliminar_usuario(self, idUser):
        self.collection.delete_one({'id': idUser})
