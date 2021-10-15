import numpy as np


class Comida:
    """Objeto contendo o nome de uma comida e seu valor nutricional.

    Parametros
    ----------
        nome : str
            Nome da comida
        array : np.array
            Array contendo 4 valores, respectivamente:
            Kilocalorias, proteínas, lipídios e carboidratos **por grama** do alimento.

        De preferência use o TBCA pra achar a informação nutricional e divida o
        array por 100.

    Exemplo
    -------
    >>> abacate = Comida('abacate', np.array(
                             (75, 1.15, 6.21, 1.81)
                         ) / 100)
    """
    def __init__(self, nome, array):
        self.nome = nome
        self.array = array

class Porção:
    """Objeto contendo uma comida e a quantidade.

    Parametros
    ----------
        comida : Comida
        quantity: int
            Quantidade da `comida`, em gramas.

    Exemplo
    -------
    >>> porção_de_abacate = Porção(abacate, 70)
    """
    def __init__(self, comida, quantity):
        self.comida = comida
        self.quantity = quantity  # quantity in grams

    def get_nutrition(self):
        return self.quantity * self.comida.array

    def set_quantity(self, qnt):
        self.quantity = qnt

    def show(self):
        print('{}g de {:=^20}:\n'
              'CAL: {:.2f}kcal, '
              'PRO: {:.2f}g, '
              'LIP: {:.2f}g, '
              'CAR: {:.2f}g'.format(self.quantity,
                                    self.comida.nome,
                                    *self.get_nutrition()))


class Refeição:
    """Conjunto de `Porção`s.

    Parametros
    ----------
        nome : str
            Nome da refeição.
        porção_list: iterable
            Conjunto de `Porção`s compondo a refeição.

    Exemplo
    -------
    >>> iorgas = Refeição('iorgas', [Porção(c.iogurte, 300), Porção(c.melão, 200)])
    """
    def __init__(self, nome, porção_list):
        self.nome = nome
        self.porção_list = porção_list

    def get_nutrition(self, verbose=False):
        soma = np.array((0., 0., 0., 0.))
        for porção in self.porção_list:
            soma += porção.get_nutrition()
        if verbose:
            print('Refeição - {}\n'
                  'Calorias: {:.2f}kcal\n'
                  'Proteínas: {:.2f}g\n'
                  'Lipídios: {:.2f}g\n'
                  'Carboidratos: {:.2f}g\n'.format(self.nome, *soma))
        return soma

    def show(self):
        self.get_nutrition(verbose=True)

    def show_each(self):
        for porção in self.porção_list:
            porção.show()


class Dia(Refeição):
    """Conjunto de `Refeição`s.

    Parametros
    ----------
        nome : str
            Nome da refeição.
        refeição_list: iterable
            Conjunto de `Refeição`s que compõe o dia.

    Exemplo
    -------
    >>> Dia1 = Dia('dia_foda',
                   [r.almoço, r.lanche, r.janta, r.iorgas])
    """
