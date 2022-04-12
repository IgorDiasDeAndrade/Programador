
class Canino:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = name
    def latir(self):
        self.x += 1
        return self.x
rex = Canino('rex')
lassie = Canino("lassie")
print(rex.name, Canino.latir(rex))
print(rex.name, Canino.latir(rex))
print(rex.name, Canino.latir(rex))
print(rex.name, Canino.latir(rex))
print(rex.x)
print(lassie.name, Canino.latir(lassie))
print(lassie.x)
rex = 'oi'
print(rex)

class Yorkshire(Canino):
    x = 0
    dano = 0
    def hiperativo(self):
        self.dano += 5
        print(self.name,'destruiu',self.dano,'coisas')
        #return self.dano
anduin = Yorkshire('anduin')
print(anduin.name, Canino.latir(anduin))
Yorkshire.hiperativo(anduin)
