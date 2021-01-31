from BL.ArbolBinario import ArbolBinario
from BL.Nodo import Nodo


class ArbolController(object):
    def __init__(self):
        self.arbol = ArbolBinario()
        self.root = None
        self.cont = 0

    def agregarNodo(self, info):
        nodo = Nodo(info)
        if self.cont == 0:
            self.root = self.arbol.insert(self.root, nodo)
            self.cont = self.cont+1
        else:
            self.arbol.insert(self.root, nodo)

    def obtenerInOrden(self):
        return self.arbol.inOrden(self.root)

    def obtenerPreOrden(self):
        return self.arbol.preOrden(self.root)

    def obtenerPostOrden(self):
        return self.arbol.postOrden(self.root)