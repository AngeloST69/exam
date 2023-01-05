class Persona:
    id_p   = int
    nombre = str

    def __init__(self, id_p, nombre):
        self.id_p       = id_p
        self.nombre     = nombre
        
    def __str__(self):
        return f'El id de la persona es: {self.id_p} y su nombre es: {self.nombre}'
    