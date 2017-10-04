#!/usr/bin/env python3

"""
Utilitário de linha de comando para buscar caracteres Unicode por nome
"""


def analisar(linha):
    partes = linha.split(';')
    caractere = chr(int(partes[0], 16))
    nome = partes[1]
    return (caractere, nome)


def filtrar(arquivo, consulta):
    consulta = consulta.upper()
    for linha in arquivo:
        linha = linha.strip()
        if not linha:
            continue
        caractere, nome = analisar(linha)
        if consulta in nome:
            yield caractere, nome


def listar(*palavras):
    consulta = ' '.join(palavras)
    with open('UnicodeData.txt') as arq:
        for caractere, nome in filtrar(arq, consulta):
            código = ord(caractere)
            print(f'U+{código:04X}', caractere, nome, sep='\t')


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print(f'Modo de usar:\n\t{sys.argv[0]} palavra1 palavra2 ...')
        sys.exit(1)
    listar(*sys.argv[1:])
