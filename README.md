# Gerenciador de dieta

Utilitário para gerenciar dieta, contando kilocalorias e os principais macronutrientes (proteínas, lipídios e carboidratos).
-

Os dados são estruturados da seguinte forma:
- uma `Comida` é um ingrediente com seu valor nutricional (por grama do alimento);
- uma `Porção` é uma comida com sua quantidade (em gramas);
- uma `Refeição` armazena uma sequência de `Porção`s;
- um `Dia` armazena uma sequência `Refeição`s;
- uma `Semana` armazena uma sequência de `Dia`s.

As classes `Refeição`, `Dia` e `Semana` são filhas de uma classe abstrata que funciona de forma recursiva chamada `RangoTree`.

O esquema abaixo ilustra a ideia das `RangoTree`s (mais informação sobre pode ser encontrada no código (`core.py`)):

<p align="center">
  <img src="https://github.com/chedieck/diet-manager/blob/master/src/rangotree_scheme.png" />
</p>


No arquivo `comidas.py` há exemplos de `Comida`s e no arquivo `rotina.py` há exemplos de organizações de rotina: refeições, dias e semanas.

<p align="center">
  <img src="https://github.com/chedieck/diet-manager/blob/master/src/rotina_screenshot.png" />
</p>
