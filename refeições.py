from core import Refeição, Porção
import comidas as c

café = Refeição(
    'café',
    [Porção(c.ovo, 50), Porção(c.bacon_cru, 70)]
)
almoço = Refeição(
    'almoço',
    [Porção(c.coração_frango, 576), Porção(c.manteiga, 15), Porção(c.abobrinha_crua, 90)]
)
lanche = Refeição(
    'lanche',
    [Porção(c.avelã, 70), Porção(c.iogurte, 300), Porção(c.abacate, 70)]
)
janta = Refeição(
    'janta',
    [Porção(c.coração_frango, 500), Porção(c.manteiga, 15)]
)
iorgas = Refeição(
    'iorgas',
    [Porção(c.iogurte, 300), Porção(c.melão, 200)]
)

# Cecília
café_cecília = Refeição(
    'café_cecília',
    [Porção(c.ovo, 150), Porção(c.amendoim, 20)]
)
lanche_cecília = Refeição(
    'lanche_cecília',
    [Porção(c.whey, 33), Porção(c.morango, 85)]
)
almoço_cecília = Refeição(
    'almoço_cecília',
    [Porção(c.peito_frango, 100), Porção(c.batata_baroa_cozida, 80), Porção(c.azeite, 18)]
)
lanche_cecília_2 = Refeição(
    'lanche_cecília',
    [Porção(c.whey, 33), Porção(c.morango, 100)]
)
janta_cecília = Refeição(
    'janta_cecília',
    [Porção(c.atum_enlatado_óleo, 120), Porção(c.tomate, 100), Porção(c.maionese_light, 30)]
)
# ENDREGION
