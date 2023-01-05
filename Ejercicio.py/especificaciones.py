from persona import Persona
from computador import Computador
from computador import Info
from marca import Marca
from gama import Gama

class Especificaciones:
    procesador      = str
    pantalla        = str
    RAM             = str
    computador      = Info("","","","","")
    persona         = Persona("","")
    marca           = Marca("","")
    gama            = Gama("","")
    
    
    #Herencia dentro de otro archivo
    
    def __init__(self, procesador, pantalla , RAM, computador, persona, marca, gama):
        self.procesador     = procesador
        self.pantalla       = pantalla     
        self.RAM            = RAM
        self.computador     = computador
        self.persona        = persona
        self.marca          = marca
        self.gama           = gama