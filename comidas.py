import numpy as np

from core import Comida

## REGION FRUTAS
abacate = Comida(
    'abacate',
    np.array((75, 1.15, 6.21, 1.81)) / 100,
)
banana = Comida(
    'banana',
    np.array((109, 1.27, 0.19, 26.7)) / 100,
)
morango = Comida(
    'morango',
    np.array((30, 0.82, 0.4, 6.54)) / 100,
)
melão = Comida(
    'melão',
    np.array((24, 0.61, 0.15, 5.7)) / 100,
)
## ENDREGION

## REGION CARNES, sempre s/ óleo s/ sal
# porco
bacon = Comida(
    'bacon',
    np.array((689, 27.4, 64.3, 0.44)) / 100,
)  # frito
bacon_cru = Comida(
    'bacon_cru',
    np.array((599, 9.76, 61.5, 1.64)) / 100,
)
costela_assada = Comida(
    'costela assada',
    np.array((398, 30.2, 30.3, 1.2)) / 100,
)
# galinha
ovo = Comida(
    'ovo',
    np.array((125, 10.4, 8.7, 1.3)) / 100,
)  # cru
peito_frango_cru = Comida(
    'peito de frango cru',
    np.array((102, 21, 2, 0)) / 100,
)
peito_frango = Comida(
    'peito de frango',
    np.array((150, 32, 2.4, 0)) / 100,
)  # grelhado
coração_frango = Comida(  # coz/cru = 0.6875
    'coração de frango',
    np.array((201, 22.4, 12.1, 0.61)) / 100,
)  # grelhado
coxinha_asa = None  # coz/cru = 0.80; (cozido) sem_osso/ com_osso = 0.633
# peixe
atum_enlatado_óleo = Comida(
    'atum enlatado no óleo',
    np.array((187, 23.6, 9.8, 1.23)) / 100,
)
tilápia = Comida(
    'tilápia cozida',
    np.array((454, 22.2, 2.07, 0)) / 100
)

## ENDREGION

# Queijos
queijo_colonial_deale = Comida(
    'queijo colonial deale',
    np.array((84, 5.8, 6.5, 0.7)) / 30,
)
muçarela_búfula_bom_destino = Comida(
    'muçarela búfula bom destino',
    np.array((79, 7.5, 5.1, 1)) / 30,
)
queijo_cabra_frescal_machevre_caprivama = Comida(
    'queijo cabra frescal machevre caprivama',
    np.array((82, 6, 8, 0)) / 30,
)

# CASTANHAS
amendoim = Comida(
    'amendoim',
    np.array((625, 27.5, 51.8, 16.9)) / 100,
)  # torrado
avelã = Comida(
    'avelã',
    np.array((673, 15, 62.4, 17.6)) / 100,
)  # cru
castanha_caju = Comida(
    'castanha_caju',
    np.array((616, 20.7, 49.5, 24)) / 100,
)  # torrado

# DERIVADOS
creme_leite = Comida(
    'creme_leite',
    np.array((27, 0, 3, 0.49)) / 15,
)
manteiga = Comida(
    'manteiga',
    np.array((750, 0, 82, 0)) / 100,
)
iogurte = Comida(
    'iogurte',
    np.array((62, 3.97, 1.82, 7.61)) / 100,
)
leitíssimo = Comida(
    'leite leitíssimo',
    np.array((136, 6.9, 8, 9.1)) / 200,
)


# CARBS
batata_baroa_cozida = Comida(
    'batata_baroa_cozida',
    np.array((77, 0.85, 0.17, 18.9)) / 100,
)

# verduras
# carbs vegetal/100g: abobrinha=3.4, cebola=7.1, pimentão=2.78, quiabo=2.45
# alho: 25.8
vegetal = Comida(
    'vegetal',
    np.array((20, 0, 0, 3)) / 100,
)  # estimativa, isso aqui não existe kkkkkkkk
abobrinha_crua = Comida(
    'abobrinha',
    np.array((17, 1.01, 0.12, 3.71)) / 100,
)
tomate = Comida(
    'tomate',
    np.array((17, 1.04, 0.17, 3.82)) / 100,
)

# else
azeite = Comida(
    'azeite',
    np.array((900, 0, 100, 0)) / 100,
)
mel = Comida(
    'mel',
    np.array((328.39, 0.17, 0, 80.9)) / 100,
)
whey = Comida(
    'whey',
    np.array((129, 23, 2.6, 3.3)) / 33,
)
coco_ralado = Comida(
    'coco_ralado',
    np.array((67, 0.6, 6.7, 0.9)) / 12,
)
maionese_light = Comida(
    'maionese_light',
    np.array((238, 0.37, 22.2, 9.23)) / 100,
)
