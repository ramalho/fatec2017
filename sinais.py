#!/usr/bin/env python3

"""
Utilitário de linha de comando para buscar caracteres Unicode por nome
"""


def analisar(linha):
    partes = linha.split(';')
    caractere = chr(int(partes[0], 16))
    nome = partes[1]
    palavras = set(nome.replace('-', ' ').split())
    if partes[10]:
        nome += f' ({partes[10]})'
        palavras |= set(partes[10].replace('-', ' ').split())
    return (caractere, nome, palavras)


def filtrar(arquivo, consulta):
    consulta = set(consulta.upper().replace('-', ' ').split())
    for linha in arquivo:
        linha = linha.strip()
        if not linha:
            continue
        caractere, nome, palavras = analisar(linha)
        if consulta <= palavras:
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
