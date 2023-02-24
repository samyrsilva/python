def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
         quantidade = len(x)
         contador.append(quantidade)
    return contador
if __name__ == '__main__':
   lista = ('coa7cuu', 'gato','caccdcd','perara','nome')
print(contador_letras(lista))

contador_letras = lambda  lista: [len(x) for x in lista]
lista_animais = ['gat88rrr888rro','casa','bote']
print(contador_letras(lista_animais))