from zona import Zona

class Zoologico:
    def __init__(self, nombre, ubicacion) -> None:
        self._nombre: str = nombre
        self._ubicacion: str = ubicacion
        self._zonas = [] #0 ó más 

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubi):
        self._ubicacion = ubi

    def getZonas(self):
        return self._zonas
    def setNombre(self, zonas):
        self._zonas = zonas

    def agregarzonas(self, zona): 
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        total = 0
        for x in self._zonas:
            total += x.cantidadAnimales()
        return total
