from core import Porção, Refeição, Dia, Semana
import comidas as c


# refeições
café = Refeição(
    'café',
    [Porção(c.ovo, 50), Porção(c.bacon_cru, 70)]
)
almoço = Refeição(
    'almoço',
    [Porção(c.coração_frango, 576 * 0.6875), Porção(c.manteiga, 15), Porção(c.abobrinha_crua, 90)]
)
lanche = Refeição(
    'lanche',
    [Porção(c.avelã, 70), Porção(c.iogurte, 300), Porção(c.abacate, 70)]
)
janta = Refeição(
    'janta',
    [Porção(c.coração_frango, 500 * 0.6875), Porção(c.manteiga, 15)]
)
iorgas = Refeição(
    'iorgas',
    [Porção(c.iogurte, 300), Porção(c.melão, 200)]
)

# dias
segunda = Dia('Segunda-feira',
              [café, almoço, lanche, janta])
terça = Dia('Terça-feira do iogurte',
            [iorgas, almoço, iorgas])

# semana
semana = Semana('Semana exemplo',
                [segunda, terça])

if __name__ == '__main__':
    # almoço.get_tree_info()
    segunda.get_tree_info()
    # semana.get_tree_info()

