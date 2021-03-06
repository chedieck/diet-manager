import numpy as np
import re
from abc import ABC


class Comida:
    """Objeto contendo o nome de uma comida e seu valor nutricional.

    Parametros
    ----------
        nome : str
            Nome da comida
        kplc_array : np.array
            Array contendo 4 valores, respectivamente:
            Kilocalorias, proteínas, lipídios e carboidratos **por grama** do alimento.

        De preferência use o TBCA pra achar a informação nutricional e divida o
        array por 100.
        http://www.tbca.net.br/base-dados/composicao_estatistica.php

    Exemplo
    -------
    >>> abacate = Comida('abacate', np.array(
                             (75, 1.15, 6.21, 1.81)
                         ) / 100)
    """
    def __init__(self, nome, kplc_array):
        self.nome = nome
        self.kplc_array = kplc_array


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

    @property
    def title(self):
        simple_title = f'{self.quantity}g de {self.comida.nome}: '
        return f'{simple_title:<30}'


    def __str__(self):
        """Informação nutricional da porção.

        'K' := Kilocalorias
        'P' := Proteínas
        'L' := Lipídios
        'C' := Carboidratos
        """
        nutrition = self.get_nutrition()
        calories = f'K {nutrition[0]:.2f}kcal'
        proteins = f'P {nutrition[1]:.2f}g'
        lipids = f'L {nutrition[2]:.2f}g'
        carbs = f'C {nutrition[3]:.2f}g'
        return (self.title
                + f'{calories:<15} {proteins:<12} {lipids:<12} {carbs:<12}')

    def get_nutrition(self):
        return self.quantity * self.comida.kplc_array

    def set_quantity(self, qnt):
        self.quantity = qnt


class RangoTree(ABC):
    """Classe abstrata para agrupar `Porção`s ou `RangoTree`s.

    Funciona recursivamente: um `RangoTree` guarda um conjunto de `Porção`s ou de
    `RangoTree`s. Não pode guardar um conjunto contendo ambos `RangoTree` e `Porção`.
    Se conter um conjunto de `RangoTree`s, estes também podem conter um conjunto
    de `RangoTree`s. As folhas dessa árvore, por fim, devem necessariamente ser
    do tipo `Porção`s.
    

    Parametros
    ----------
        nome : str
            Nome da refeição.
        porção_or_rango_list: subscritable iterable
            Iterável indexável (e.g. `list`) de `Porção`s ou `RangoTree`s.

    Cheque as classes filhas `Refeição` e `Dia` para ver como usá-las.
    """
    def __init__(self, nome, porção_or_rango_list):
        self.nome = nome
        self.porção_or_rango_list = porção_or_rango_list

        # validate
        if len(porção_or_rango_list) == 0:
            raise ValueError("Tentando criar `RangoTree` com lista vazia.")
        if len(set(type(obj) for obj in self.porção_or_rango_list)) > 1:
            raise ValueError("Tentando criar `RangoTree` com lista contendo mais de um tipo.")
        if not self.are_leafs_porção():
            raise ValueError("Tendtando criar `RangoTree` tal que as folhas não são `Porção`s.")

    def has_porção_list(self):
        """Retorna verdadeiro se conter uma lista de `Porção`s.
        """
        first_obj = self.porção_or_rango_list[0]
        if type(first_obj) == Porção:
            return True
        return False

    def are_leafs_porção(self):
        """Checa se as folhas da árvore são do tipo `Porção`.
        """
        if self.has_porção_list():
            return True
        else:
            return self.porção_or_rango_list[0].are_leafs_porção()

    @property
    def title(self):
        class_name = self.__class__.__name__
        return f'> {self.nome} ({class_name})\n'

    @property
    def porção_info(self):
        if not self.has_porção_list():
            return ''
        return '  +' + '\n  +'.join(map(str, self.porção_or_rango_list)) + '\n'

    def __str__(self):
        """Informação nutricional da porção.

        'K' := Kilocalorias
        'P' := Proteínas
        'L' := Lipídios
        'C' := Carboidratos
        """
        nutrition_arr = self.get_nutrition(verbose=True)
        separator = ''
        if self.has_porção_list():
            separator = ('  '
                         + '=' * max(map(
                             len,
                             self.porção_info.split('\n')
                         )) + '\n')
        return (self.title +
                separator +
                self.porção_info +
                separator +
                '  K: {:.2f}kcal\n'
                '  P: {:.2f}g\n'
                '  L: {:.2f}g\n'
                '  C: {:.2f}g\n'.format(*nutrition_arr))

    def get_nutrition(self, verbose=False):
        total = np.array((0., 0., 0., 0.))
        for porção in self.porção_or_rango_list:
            total += porção.get_nutrition()
        return total

    def idented_str(self, n):
        base = str(self)
        # ident title
        prefix = '----' * n if n else '>'
        if n:
            prefix = prefix + '>'
        base = base.replace('>', prefix)

        # ident nutrition
        prefix = '\n  ' + n * '    '
        base = re.sub(r'\n  ([KPLC]|\+|=)', prefix + r'\1', base)

        return base


    def get_tree_info(self, n=0, verbose=True):
        """Mostra ou retorna toda informação nutricional contida no objeto.
        
        Parametros
        ----------

        n : int, optional
            Usado pra identar a informação nutricional, indica a profundidade
            da recursividade. Argumento privado.
        verbose : bool, optional
            Se verdadeiro, apenas printa a informação e retorna None. Se falso,
            não printa a informação mas a retorna como string.

        """
        to_print = self.idented_str(n)
        for porção in self.porção_or_rango_list:
            if hasattr(porção, 'get_tree_info'):
                to_print += porção.get_tree_info(n=n + 1,
                                             verbose=False)

        if verbose:
            print(to_print)
            return
        return to_print


class Refeição(RangoTree):
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


class Dia(RangoTree):
    """Conjunto de `Refeição`s.

    Parametros
    ----------
        nome : str
            Nome da refeição.
        refeição_list: iterable
            Conjunto de `Refeição`s que compõe o dia.

    Exemplo
    -------
    >>> segunda = Dia('Segunda-feira',
                   [r.almoço, r.lanche, r.janta, r.iorgas])
    """


class Semana(RangoTree):
    """Conjunto de `Dia`s.

    Parametros
    ----------
        nome : str
            Nome da semana.
        dia_list: iterable
            Conjunto de `Dia`s que compõe a semana.

    Exemplo
    -------
    >>> semana_1 = Semana('Primeira semana',
                   [d.segunda, d.terça, d.quarta, d.quinta, d.sexta, d.sábado, d.domingo]
                   )
    """


class MacroMeta:
    """
    Meta de macros para atingir.

    Define um limite superior e inferior para cada macro (kcal, proteínas,
    lipídios e carboidratos). Não é necessário definir nenhum dos limites,
    qualquer parametro que não for passado indicará que o macro referente
    não é importante.

    Parametros
    ----------
    kcal : Union[None, tuple[int]]
        Limites para kilocalorias (min, max).
    prot : Union[None, tuple[int]]
        Limites para proteínas, em gramas (min, max).
    lip : Union[None, tuple[int]]
        Limites para lipídios, em gramas (min, max).
    carb : Union[None, tuple[int]]
        Limites para carboidratos, em gramas (min, max).

    Exemplos
    --------
    >>> # mínimo de 2800 kcal, nenhum limite máximo.
    >>> MacroMeta(kcal=(2800, None))
    >>> # entre 1600 e 1900 kcal, máximo de 30g de carboidratos.
    >>> m = MacroMeta(kcal=(1600, 1900),
                  carb=(None, 30))
    >>> m.check(d.segunda)
    """

    def __init__(self, kcal: tuple = None, prot: tuple = None, lip: tuple = None, carb: tuple = None):
        self.metas_dict = {
            'kcal': kcal,
            'prot': prot,
            'lip': lip,
            'carb': carb,
        }

    def _unit_and_name_str(self, macro_key):
        if macro_key == 'kcal':
            return 'kcal'
        if macro_key == 'prot':
            return 'g de proteínas'
        if macro_key == 'lip':
            return 'g lipídeos'
        if macro_key == 'carb':
            return 'g de carboidratos'

    def _get_macro_status_str(self, macro_key, valor):
        macro_meta = self.metas_dict.get(macro_key)
        if macro_meta is None:
            return ""

        limite_inferior = macro_meta[0]
        limite_superior = macro_meta[1]
        unit_and_name_str = self._unit_and_name_str(macro_key)

        if limite_inferior:
            if valor < limite_inferior:
                return f"Faltam {limite_inferior - valor:.2f}{unit_and_name_str}.\n"
        if limite_superior:
            if valor > limite_superior:
                return f"Extra {limite_inferior - valor:.2f}{unit_and_name_str}.\n"
        return f"Objetivo atingido: {valor:.2f}{unit_and_name_str}"


    def _get_macro_key_for_index(self, idx):
        if idx == 0:
            return 'kcal'
        if idx == 1:
            return 'prot'
        if idx == 2:
            return 'lip'
        if idx == 3:
            return 'carb'

    def check(self, rango_tree):
        total_str = ""
        for idx, valor in enumerate(rango_tree.get_nutrition()):
            macro_key = self._get_macro_key_for_index(idx)
            total_str += self._get_macro_status_str(macro_key, valor)
        total_str = total_str.rstrip('\n')

        print(total_str)


