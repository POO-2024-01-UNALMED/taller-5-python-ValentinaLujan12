from gestion.zona import Zona
class Animal:
    def __init__(self, totalAnimales, nombre, edad, habitat, genero, zona) -> None:
        self._totalAnimales: int = totalAnimales
        self._nombre: str = nombre
        self._edad: int = edad
        self._habitat: str 
        self._genero: str
        self._zona: Zona #0 ó 1

    def getTotalAnimales(self):
        return self._totalAnimales
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getZoo(self):
        return self._zoo
    def setZoo(self, zoo):
        self._zoo = zoo

    def getAnimales(self):
        return self._animales
    def setAnimales(self, animal):
        self._animales = animal

    def movimiento():
        pass

    def totalPorTipo():
        pass

    def __str__(self) -> str:
        pass
