from collections import Counter
from unidecode import unidecode

with open('arquivo.txt', 'r') as arquivo_txt:
    texto = arquivo_txt.read()

def carregar_arquivo(arquivo):
    with open(arquivo, 'r') as arquivo_txt:
        texto = arquivo_txt.read()
    return unidecode(texto)

def contar_palavras(texto):
    palavras = texto.lower().split()
    contador_palavras = Counter(palavras)
    ranking = contador_palavras.most_common()
    for palavra, frequencia in ranking:
        print(f'{palavra}: {frequencia}')
        
def procurar_palavras(texto):
    palavras = texto.lower().split()
    contador_palavras = Counter(palavras)
    palavras_procuradas = input('Digite as palavras que deseja procurar (se for mais de uma, separe as palavras por vírgula): ').split(',')
    for palavra in palavras_procuradas:
        frequencia = contador_palavras.get(palavra.strip(), 0)
        print(f'A palavra: "{palavra.strip()}", aparece: {frequencia} vezes no arquivo.')
        
def exibir_frequencia(texto):
    palavras = texto.lower().split()
    contador_palavras = Counter(palavras)
    palavra_mais_frequente = contador_palavras.most_common(1)[0][0]
    frequencia_maior = contador_palavras.most_common(1)[0][1]
    palavra_menos_frequente = contador_palavras.most_common()[-1][0]
    frequencia_menor = contador_palavras.most_common()[-1][1]
    print(f'A palavra com mais aparições é "{palavra_mais_frequente}" com o total de {frequencia_maior} aparições.')
    print(f'A palavra com menos aparições é "{palavra_menos_frequente}" com o total de {frequencia_menor} aparições.')
    
while True:
    print('\nMenu de opções:')
    print('1 - Carregar arquivo de texto e retirar acentos')
    print('2 - Contar as palavras e exibir em um ranking')
    print('3 - Procurar por palavras específicas')
    print('4 - Exibir palavra com mais e menos frequente')
    print('0 - Encerrar')
    opcao = input('\nEscolha uma opção: ')
    
    if opcao == '1':
        arquivo = input('Digite o nome do arquivo: ')
        texto = carregar_arquivo(arquivo)
        print(f'Texto carregado:\n\n{texto}\n')
        
    elif opcao == '2':
        contar_palavras(texto)
            
    elif opcao == "3":
        print(procurar_palavras(texto))
       
    elif opcao == '4':
            exibir_frequencia(texto)
            
    elif opcao == '0':
        print('Encerrando a aplicação. Obrigada, até breve!')
        break
    else:
        print('Opção inválida')