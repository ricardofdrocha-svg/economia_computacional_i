import es
from aritmetico import soma
from matematica.conjuntos import inteiros



def main():
    # Entrada de dados
    dados = es.leitura_dados()

    # Processamento
    resultado = soma(dados[0], dados[1])

    # Saída
    es.saida(dados, resultado)

if __name__ == '__main__':
    main()

