class Visitable:
    def acepta(self, visitante):
nombre_classe = self.__class__.__name__
metodo = getattr(visitante, 'visita{}'.format(nombre_clase),
'default')
        metodo(self)
# Hacemos heredar de Visitable todas las clases de sintaxis.
visitante = Visitante()
bucle.acepta(visitante)
