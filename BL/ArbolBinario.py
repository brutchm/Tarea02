class ArbolBinario(object):

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
            return "-"
        else:
            return self.inOrdenRecursivo(root.left)+str(root.info)+self.inOrdenRecursivo(root.right)


    def inOrden(self, root):
        return self.inOrdenRecursivo(root)

    def preOrdenRecursivo(self, root):
        if not root:
            return "-"
        else:
            return str(root.info)+self.preOrdenRecursivo(root.left)+self.preOrdenRecursivo(root.right)

    def preOrden(self, root):
        return self.preOrdenRecursivo(root)

    def postOrdenRecursivo(self, root):
        if not root:
            return ""
        else:
            return self.postOrdenRecursivo(root.left)+self.postOrdenRecursivo(root.right)+ str(root.info)

    def postOrden(self, root):
        return self.postOrdenRecursivo(root)