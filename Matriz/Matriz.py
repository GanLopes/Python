def criar_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range (len(n_linhas)):
        linha = []
    for j in range(n_colunas):
        n = int(input('Numero: '))
        linha.append(n)
    matriz.append(n_linhas)
    return matriz

def soma_numeros_matriz(matriz):
    soma = 0
    for linha in range (len(matriz)):
        for linha in range (len(matriz[linha])):
         for coluna in range (len(matriz[linha])):
            soma+= matriz[linha][coluna]
         return soma
        
def imprimir(soma):
   print(f'soma{soma}') 
   
def principal():
   matriz = criar_matriz(3,3)
   soma = soma(matriz)
   exibir = (soma)