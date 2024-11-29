def algoritmo_a_b():
    # Dados duas strings, a e b, onde a = “João” e b = “Maria”, 
    # como fazer com que as duas variáveis troquem de valores, ou seja, a = “Maria” e b = “João”?
    a = "Joao"
    b = "Maria"

    c = a       # c = "Joao"
    a = b       # a = "Maria"
    b = c       # b = "Joao"

def soma(num1 : int, num2 : int) -> int:
    ''' Função que calcula a soma de dois numeros *num1* e *num2*
    '''
    return num1 + num2

def determina_area(largura : float, comprimento: float ) -> float:
    ''' Função que calcula a área de um quadrilátero
    '''
    return largura * comprimento

def verifica_par(num : int ) -> bool:
    ''' Função que verifica se o número *num* é par
    '''
    return num % 2 == 0

def converte_horas(minutos : int) -> float:
    return minutos / 60

def frase_n(frase : str, n : int) -> str:
    return (frase + n * "!")

def dados_aluno(nome : str, idade : int, ra : int) -> str:
    return (nome + " - " + str(idade) + " - " + str(ra) )

def classificar_idade(idade : int) -> str:
    ''' Função que classifica uma pessoa de acordo com sua idade
    '''

    if idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 64:
        return "Adulto"
    else:
        return "Idoso"


print(dados_aluno("vinicius", 13,12019))

print(classificar_idade(12))