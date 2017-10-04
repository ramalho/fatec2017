#!/usr/bin/env python3

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


if __name__ == '__main__':
    import sys
    consulta = ' '.join(sys.argv[1:])
    with open('UnicodeData.txt') as arq:
        for caractere, nome in filtrar(arq, consulta):
             print(caractere, nome) 



