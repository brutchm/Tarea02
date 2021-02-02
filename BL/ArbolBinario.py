from BL.Nodo import Nodo


class ArbolBinario(object):

    def __init__(self):
        self.root=None

    def inicializarRoot(self, val):
        if self.root == None:
            nodo = Nodo(val)
            self.root=nodo

    def insert(self,root, node):
        if root is None:
            return node
        if root.info < node.info:
            root.right = self.insert(root.right, node)
        else:
            root.left = self.insert(root.left, node)
        return root

    def inOrdenRecursivo(self, root):
        if not root:
            return ""
        else:
            return self.inOrdenRecursivo(root.left)+str(root.info)+","+self.inOrdenRecursivo(root.right)


    def inOrden(self):
        return self.inOrdenRecursivo(self.root)

    def preOrdenRecursivo(self, root):
        if not root:
            return ""
        else:
            return str(root.info)+","+self.preOrdenRecursivo(root.left)+self.preOrdenRecursivo(root.right)

    def preOrden(self):
        return self.preOrdenRecursivo(self.root)

    def postOrdenRecursivo(self, root):
        if not root:
            return ""
        else:
            return self.postOrdenRecursivo(root.left)+self.postOrdenRecursivo(root.right)+ str(root.info)+","

    def postOrden(self):
        return self.postOrdenRecursivo(self.root)