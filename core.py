import numpy as np
import re


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

    def __str__(self):
        return ('{}g de {:=^20}:\n'
                'CAL: {:.2f}kcal, '
                'PRO: {:.2f}g, '
                'LIP: {:.2f}g, '
                'CAR: {:.2f}g'.format(self.quantity,
                                      self.comida.nome,
                                      *self.get_nutrition()))


    def get_nutrition(self):
        return self.quantity * self.comida.array

    def set_quantity(self, qnt):
        self.quantity = qnt

    def show(self):
        print(str(self))

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

    @property
    def title(self):
        class_name = self.__class__.__name__
        return f'> {self.nome} ({class_name})\n'

    def __str__(self):
        nutrition_arr = self.get_nutrition(verbose=True)
        return (self.title +
                '  Calorias: {:.2f}kcal\n'
                '  Proteínas: {:.2f}g\n'
                '  Lipídios: {:.2f}g\n'
                '  Carboidratos: {:.2f}g\n'.format(*nutrition_arr))

    def get_nutrition(self, verbose=False):
        total = np.array((0., 0., 0., 0.))
        for porção in self.porção_list:
            total += porção.get_nutrition()
        return total

    def show(self):
        print(str(self))

    def show_each(self):
        for porção in self.porção_list:
            porção.show()

    def idented_str(self, n):
        base = str(self)
        # ident title
        prefix = '----' * n if n else '>'
        if n:
            prefix = prefix[1:] + '>'
        base = base.replace('>', prefix)

        # ident nutrition
        prefix = '\n  ' + n * '    '
        base = re.sub(r'\n  ([A-Z])', prefix + r'\1', base)
        return base


    def get_tree_info(self, n=0, verbose=True):
        to_print = self.idented_str(n)
        for porção in self.porção_list:
            if hasattr(porção, 'get_tree_info'):
                to_print += porção.get_tree_info(n=n + 1,
                                             verbose=False)
            else:
                to_print += ''# str(porção)

        if verbose:
            print(to_print)
        return to_print


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
