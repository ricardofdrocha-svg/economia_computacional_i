# Projeto v. 0.0.2

## Projeto de interface com o usuário

<!-- A partir dos requisitos criar uma interface com o usuário seja ela de texto (isto é, disponível no terminal de linha de comando) seja ela ou gráfica.-->

A interface será de linha de comando.
## Tipo de aplicação e arquitetura

<!--
O tipo de aplicação define a melhor arquitetura e esta, por sua vez, define o paradigma de programação mais adequado a ser usado. As decisões aqui tomadas dizem respeito a decisões referentes à organização do código em funções, métodos, classes, módulos, subpacotes e pacotes. Aquiu também se pode definir a melhor linguagem de programação a ser utilizada -->

A aplicação conterá dois módulos Python ambos dentro de um único pacote. Os nomes dos módulos serão os seguintes nome:

1. __main__
2. LivroTexto


## Projeto de dados e algoritmos

<!-- Os dados deverão ser alocados em estruturas de dados nativas ou classe criadas pelo programador. Os algoritmos estarão implementados nas funções ou métodos a depender do paradigma de programação utilizado -->

A classe LivroTexto deverá conter os seguintes atributos e tipos:
1. titulo: str
2. autor: str
3. preco: float

Haverá um método com a seguinte assinatura:

valor_desconto(percentual_desconto: float) -> float