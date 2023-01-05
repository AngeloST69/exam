from persona import Persona
from computador import Computador
from computador import Info
from marca import Marca
from gama import Gama
from especificaciones import Especificaciones

class Especificaciones2(Especificaciones):
    procesador_c    = str
    pantalla_c      = str

    
    #Herencia dentro de otro archivo
    
    def __init__(self, procesador, pantalla, RAM, computador, persona, marca, gama, procesador_c, pantalla_c):
        super().__init__(procesador, pantalla, RAM, computador, persona, marca, gama)

        self.procesador_c   = procesador_c
        self.pantalla_c     = pantalla_c
        
