from core import Dia
import refeições as r


Dia1 = Dia('teste',
           [r.café, r.almoço, r.lanche, r.janta, r.iorgas])

# cecília
Dia1_cecília = Dia('dia teste cecília',
                    [r.café_cecília,
                     r.lanche_cecília,
                     r.almoço_cecília,
                     r.lanche_cecília_2,
                     r.janta_cecília])


if __name__ == '__main__':
    # almoço.show_each()
    # almoço.show()
    Dia1.show()
    print('========' * 4)
    Dia1.show_each()
