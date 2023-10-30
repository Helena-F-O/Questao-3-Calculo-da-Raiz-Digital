# Questao-3-Calculo-da-Raiz-Digital
Questão 3 da avaliação N2 de Desenvolvimento Ágil

Academica: Helena Felicia de Oliveira Avelino e José Vitor Vegini

Fase:6

Engenharia de Software

Questão 3: Cálculo da Raiz Digital

Você deve implementar uma função chamada digital_root(n) que calcula a raiz digital de um número não negativo. A raiz digital é a soma recursiva de todos os dígitos de um número até que reste apenas um dígito.

A função deve receber um número inteiro não negativo n como entrada e retornar o dígito único resultante após a aplicação do processo de soma recursiva.

Aqui está um exemplo de como a função deve funcionar:

>>> digital_root(16)
7
>>> digital_root(942)
6
>>> digital_root(132189)
6
>>> digital_root(493193)
2
 

Você também deve criar pelo menos 4 testes unitários para garantir que a função está funcionando corretamente em diferentes casos.

Lembre-se de seguir as boas práticas de programação, fornecer comentários apropriados e garantir que sua função seja eficiente.

Instruções para Testes Unitários:

Você deve criar testes unitários para verificar se a função digital_root está funcionando corretamente. Certifique-se de cobrir diferentes cenários, incluindo números com vários dígitos e números com um único dígito. Certifique-se de incluir comentários explicando o propósito de cada teste.

Exemplo de teste unitário:

 

def test_digital_root():
    assert digital_root(16) == 7  # Teste para número de dois dígitos

 

Por favor, desenvolva a função e os testes unitários com base nas instruções fornecidas.  
