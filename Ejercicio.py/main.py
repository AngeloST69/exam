from persona import Persona
from computador import Computador
from computador import Info
from especificaciones import Especificaciones
from gama import Gama
from marca import Marca
from especificaciones2 import Especificaciones2

if __name__ == "__main__":
    
    computador1     = Info(1, "Angelo", 31, "Asus 7", 2021)
    computador2     = Info(2, "Francisco", 74, "MAc", 2019)
    
    
    computador3     = Computador(3, "Gabriela", 26, "Lenovo")
    
    gama1           = Gama(30, "Media")
    gama2           = Gama(61, "Media alta")
    
    marca1          = Marca(23, "ASus")
    marca2          = Marca(54, " Apple")
    
    persona1        = Persona("32", "Angelo Lopez")
    persona2        = Persona("41", "MAriano Andres")
        
    persona3        = Persona(21, "Martin")
    persona4        = Persona(43, "Fernando")
    
    especificaciones1 = Especificaciones("Rayzen 9", "254gbsdd", "16gb", computador1, gama1, marca1, persona1)
    especificaciones2 = Especificaciones("Intel core i 7", "254gbsdd", "16gb", computador2, gama2, marca2, persona2)
    
    especificaciones3 = Especificaciones2("Intel core i 7", "16pulgadas","Intel core i 7", "254gbsdd", "16gb",computador2, gama2, marca2, persona2)
    especificaciones4 = Especificaciones2("Intel core i 7", "14pulgadas", "Rayzen 9", "254gbsdd", "16gb", computador1, gama1, marca1, persona1)
    
    
    
    #Clase con metodo
    
    print("¡¡¡¡¡¡¡¡¡¡¡Pregunta 1!!!!!!!!!")
    print(" ")
    print(persona3)
    print(persona4)
    print(vars(persona4))
    print(" ")
    
    print("¡¡¡¡¡¡¡¡¡¡¡Pregunta 2!!!!!!!!!")
    print(vars(especificaciones1))
    
    print("¡¡¡¡¡¡¡¡¡¡¡Pregunta 3!!!!!!!!!")
    print(computador1)
    print(computador2)
    
    print("¡¡¡¡¡¡¡¡¡¡¡Pregunta 4!!!!!!!!!")
    print("PERSONA")
    print(vars(persona1))
    

    
    print("CLASE CON METODO")
    print("ESPECIFICACIONES")
    print(vars(computador1))
    print(" ")
    print("COMPUTADOR")
    print(vars(computador3))
    print(" ")
    print("GAMA")
    print(vars(gama1))
    print(" ")
    print("MARCA")
    print(vars(marca1))
    print(" ")
    print("PERSONA")
    print(vars(persona1))
    print(" ")
    
    #Metodo str
    
    print("METODO STR")  
    print(computador1)
    print(" ")
    print(computador2)
    
    #Objetos dentro de objetos
    
    print("OBJETOS DENTRO DE OBJETOS")
    print( vars( especificaciones1))
    print(" ")
    print(vars(especificaciones2))