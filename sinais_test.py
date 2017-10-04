import io

from sinais import analisar, filtrar

def test_analisar_letra_A():
    linha = '00C7;LATIN CAPITAL LETTER C WITH CEDILLA;Lu;0;L;0043 0327;;;;N;LATIN CAPITAL LETTER C CEDILLA;;;00E7;'
    resultado = analisar(linha)
    assert resultado == ('Ç' , 'LATIN CAPITAL LETTER C WITH CEDILLA')


def test_analisar_menor_que():
    linha = '003C;LESS-THAN SIGN;Sm;0;ON;;;;;Y;;;;;'
    resultado = analisar(linha)
    assert resultado == ('<' , 'LESS-THAN SIGN')


def test_filtrar_menor_que():
    linha = '003C;LESS-THAN SIGN;Sm;0;ON;;;;;Y;;;;;'
    arquivo = io.StringIO(linha)
    resultado = list(filtrar(arquivo, 'less'))
    assert resultado == [('<' , 'LESS-THAN SIGN')]    

LINHAS = '''
002C;COMMA;Po;0;CS;;;;;N;;;;;
002D;HYPHEN-MINUS;Pd;0;ES;;;;;N;;;;;
002E;FULL STOP;Po;0;CS;;;;;N;PERIOD;;;;
002F;SOLIDUS;Po;0;CS;;;;;N;SLASH;;;;
0030;DIGIT ZERO;Nd;0;EN;;0;0;0;N;;;;;
0031;DIGIT ONE;Nd;0;EN;;1;1;1;N;;;;;
0032;DIGIT TWO;Nd;0;EN;;2;2;2;N;;;;;
'''

def test_filtrar_3_digitos():
    arquivo = io.StringIO(LINHAS)
    resultado = list(filtrar(arquivo, 'digit'))
    assert resultado == [
        ('0' , 'DIGIT ZERO'),
        ('1' , 'DIGIT ONE'),
        ('2' , 'DIGIT TWO'),
        ]    
    


