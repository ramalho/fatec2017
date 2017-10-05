import io

from sinais import analisar, filtrar, listar


def test_analisar_letra_A():
    linha = '0041;LATIN CAPITAL LETTER A;Lu;0;L;;;;;N;;;;0061;'
    resultado = analisar(linha)
    assert resultado == ('A', 'LATIN CAPITAL LETTER A',
                         {'A', 'CAPITAL', 'LATIN', 'LETTER'})


def test_analisar_menor_que():
    linha = '003C;LESS-THAN SIGN;Sm;0;ON;;;;;Y;;;;;'
    resultado = analisar(linha)
    assert resultado == ('<', 'LESS-THAN SIGN',
                         {'LESS', 'THAN', 'SIGN'})


def test_analizar_ponto():
    linha = '002E;FULL STOP;Po;0;CS;;;;;N;PERIOD;;;;'
    resultado = analisar(linha)
    assert resultado == ('.', 'FULL STOP (PERIOD)',
                         {'FULL', 'PERIOD', 'STOP'})


def test_analisar_colchete():
    linha = '005B;LEFT SQUARE BRACKET;Ps;0;ON;;;;;Y;OPENING SQUARE BRACKET;;;;'
    resultado = analisar(linha)
    assert resultado == ('[', 'LEFT SQUARE BRACKET (OPENING SQUARE BRACKET)',
                         {'LEFT', 'OPENING', 'SQUARE', 'BRACKET'})


def test_filtrar_menor_que():
    linha = '003C;LESS-THAN SIGN;Sm;0;ON;;;;;Y;;;;;'
    arquivo = io.StringIO(linha)
    resultado = list(filtrar(arquivo, 'less sign'))
    assert resultado == [('<', 'LESS-THAN SIGN')]


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
        ('0', 'DIGIT ZERO'),
        ('1', 'DIGIT ONE'),
        ('2', 'DIGIT TWO'),
    ]


def test_listar_cruzeiro(capsys):
    listar('cruzeiro')
    saída, _ = capsys.readouterr()
    assert saída == 'U+20A2\t₢\tCRUZEIRO SIGN\n'
