from dataclasses import dataclass

@dataclass
class Elemento:
    nombre : str

    def comparar_textos(self, texto2 : str):

        if self.nombre == texto2:
            print("Los strings son iguales.")
        print("Los strings son distintos.")

class Conjunto:

    contador = 0

    def __init__(self, lista_objetos : list, nombre : str):

        self.lista_objetos = lista_objetos
        self.nombre = nombre
        # Atributo de clase que incrementa en cada creación de un objeto de la clase.
        self.__class__.contador += 1

        @property
        def id(self):
            self.__id = self.__class__.contador
            return self.__id
        
    def contiene(self, elemento : Elemento) -> bool:

        if elemento.nombre in self.lista_objetos:
            return True
            
        return False
    
    def agregar_elemento(self, elemento : Elemento):

        if self.contiene() == False:
            self.lista_objetos.append(elemento)

    def unir(self, otro_conjunto : list):
        for elementos in otro_conjunto:
            if elementos not in self.lista_objetos:
                self.lista_objetos.append(elementos)

    def __iadd__(self, conjunto2 : list):
        self.lista_objetos.append("INTERSECTADO")
        self.lista_objetos  += conjunto2

    def __str__(self) -> str:
        return f"Conjunto: {conjunto1.lista_objetos}"
        
conjunto1 = Conjunto(lista_objetos = [1,2,3,4,5], nombre = "Lista numérica")
conjunto2 = Conjunto(lista_objetos = ["a", "b", "c", "d", 5], nombre = "Lista alfabética")