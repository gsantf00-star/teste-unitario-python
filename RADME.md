
## Uso de IA para geração de cenários de teste

  

### Função escolhida

  

multiplicar(a, b)

  

### Prompt utilizado



Crie uma tabela de planejamento de testes para a função abaixo:

  

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


  

A tabela deve conter as colunas:

- ID do teste;

- cenário;

- entrada;

- resultado esperado;

- tipo de cenário;

- observação.

  

Não gere código ainda.



Tabela gerada


| ID do teste | Cenário                                       | Entrada                         | Resultado esperado     | Tipo de cenário | Observação                                                                   |
| ----------- | --------------------------------------------- | ------------------------------- | ---------------------- | --------------- | ---------------------------------------------------------------------------- |
| T01         | Multiplicação de números positivos            | `multiplicar(3, 4)`             | `12`                   | Caso normal     | Verifica o funcionamento básico da multiplicação.                            |
| T02         | Multiplicação por zero                        | `multiplicar(5, 0)`             | `0`                    | Caso de borda   | Todo número multiplicado por zero deve resultar em zero.                     |
| T03         | Multiplicação de número positivo por negativo | `multiplicar(4, -2)`            | `-8`                   | Caso normal     | O resultado deve ser negativo.                                               |
| T04         | Multiplicação de dois números negativos       | `multiplicar(-3, -2)`           | `6`                    | Caso normal     | O resultado deve ser positivo.                                               |
| T05         | Multiplicação de números decimais             | `multiplicar(2.5, 4)`           | `10.0`                 | Caso normal     | Verifica o comportamento com valores de ponto flutuante.                     |
| T06         | Multiplicação de zero por zero                | `multiplicar(0, 0)`             | `0`                    | Caso de borda   | Avalia o comportamento quando ambos os operandos são zero.                   |
| T07         | Multiplicação com valores grandes             | `multiplicar(1000000, 1000000)` | `1000000000000`        | Caso de borda   | Verifica o comportamento com números de grande magnitude.                    |
| T08         | Entrada não numérica                          | `multiplicar("a", 2)`           | `"aa"`                 | Caso de borda   | Em Python, a multiplicação de string por inteiro é válida e repete a string. |
| T09         | Tipos incompatíveis                           | `multiplicar("a", "b")`         | Geração de `TypeError` | Caso de erro    | Strings não podem ser multiplicadas entre si.                                |



Análise de cenários



Foram aceitos os cenários principais para as funções de soma, subtração, multiplicação, divisão, potência e cálculo de média, incluindo casos normais, casos de borda e tratamento de erros. Os testes foram reorganizados para que cada cenário fosse validado por um método específico, facilitando a identificação de falhas e seguindo boas práticas de testes unitários. O cenário 0⁰ (0 elevado a 0) foi removido. Embora o Python retorne 1 para 0 ** 0, esse caso possui interpretações matemáticas diferentes e não era essencial para os objetivos da atividade. Também foram adicionados cenários extras para aumentar a cobertura dos testes, como multiplicação com números negativos e decimais, divisão com resultado decimal e tratamento de listas vazias na função calcular_media. Dessa forma, a suíte de testes ficou mais organizada, legível e com melhor cobertura dos comportamentos esperados das funções.



Código final



# test_calculadora.py

import unittest

from calculadora import dividir, multiplicar, somar, subtrair, potencia, calcular_media


class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""

    def test_calcular_media_inteiros(self):
        self.assertEqual(calcular_media([10, 8, 6]), 8)

    def test_calcular_media_decimais(self):
        self.assertAlmostEqual(
            calcular_media([5.5, 6.5, 8.0]),
            6.666666666666667
        )

    def test_calcular_media_um_numero(self):
        self.assertEqual(calcular_media([10]), 10)

    def test_calcular_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

    def test_potencia_numeros_positivos(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_potencia_expoente_zero(self):
        self.assertEqual(potencia(5, 0), 1)

    def test_potencia_base_zero(self):
        self.assertEqual(potencia(0, 5), 0)

    def test_potencia_base_negativa_expoente_impar(self):
        self.assertEqual(potencia(-2, 3), -8)

    def test_potencia_base_negativa_expoente_par(self):
        self.assertEqual(potencia(-2, 4), 16)

    def test_potencia_expoente_negativo(self):
        self.assertEqual(potencia(2, -2), 0.25)

    def test_potencia_entrada_nao_numerica(self):
        with self.assertRaises(TypeError):
            potencia("a", 2)

    def test_somar_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_somar_negativo_e_positivo(self):
        self.assertEqual(somar(-1, 1), 0)

    def test_somar_zeros(self):
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair_positivo(self):
        self.assertEqual(subtrair(10, 5), 5)

    def test_subtrair_resultado_negativo(self):
        self.assertEqual(subtrair(5, 10), -5)

    def test_subtrair_zeros(self):
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_multiplicar_por_zero(self):
        self.assertEqual(multiplicar(5, 0), 0)

    def test_multiplicar_negativo(self):
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_multiplicar_dois_negativos(self):
        self.assertEqual(multiplicar(-2, -3), 6)

    def test_multiplicar_decimais(self):
        self.assertEqual(multiplicar(2.5, 4), 10.0)

    def test_divisao_exata(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_divisao_decimal(self):
        self.assertEqual(dividir(5, 2), 2.5)

    def test_divisao_negativo(self):
        self.assertEqual(dividir(-10, 2), -5)

    def test_divisao_zero_por_numero(self):
        self.assertEqual(dividir(0, 5), 0)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)


if __name__ == "__main__":
    unittest.main()



Saída do terminal
<img width="812" height="157" alt="image" src="https://github.com/user-attachments/assets/ffe9ea2c-0602-47eb-babf-d7e32c79ce6c" />
