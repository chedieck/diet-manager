# Gerenciador de dieta

Utilitário para gerenciar dieta, contando kilocalorias e os principais macronutrientes (proteína, gordura e carboidrato).
-

Os dados são estruturados da seguinte forma:
uma `Comida` é um ingrediente com seu valor nutricional (por grama do alimento);
uma `Porção` é uma comida com sua quantidade (em gramas);
uma `Refeição` é um conjunto de porções;
um `Dia` é um conjunto de Refeições;
uma `Semana` é um conjunto de dias;

As classes `Refeição`, `Dia` e `Semana` são filhas de uma classe abstrata que funciona de forma recursiva chamada `RangoTree`.
O esquema abaixo ilustra a ideia das `RangoTree`s (mais informação sobre pode ser encontrada no código (`core.py`)):

<p align="center">
  <img src="https://github.com/chedieck/diet-manager/blob/master/src/dieta-manager.drawio.png" />
</p>


O repositório contém o arquivo `comidas.py` contendo exemplos de ingredientes com suas informações nutricionais e o arquivo `rotina.py` contém exemplos de organizações de rotina: refeições, dias e semanas.
