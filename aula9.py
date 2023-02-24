# arquivo = open('notas.txt','w')
# # arquivo.write('primeria linha escrita')
# arquivo.close()

def escrever_arquivo(texto):
    arquivo = open('teste2.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    #print (aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
         lista_notas = x.split(',')
         aluno = lista_notas [0]
         #notas = lista_notas.pop()
         lista_notas.pop(0)
         print(aluno)
         print(lista_notas)
        #for y in lista_notas
         media = lambda notas: sum([int(i) for i in notas])/ 4
         print(media(lista_notas))
         lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo,'c:/users/samyr.silva/notas2.txt')

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo,
                'c:/Users/samyr.silva/workspace/')

if __name__ == '__main__':
    #lista_media = media_notas('notas.txt')
    #print(lista_notas)
    move_arquivo('notas.txt')
    # atualizar_arquivo('terceira linha.\n')
    # escrever_arquivo ('terceira linha.\n')
    # ler_arquivo('teste2.txt')
    #  aluno = 'Cesar,7,9,3,8 \n'
    #  atualizar_arquivo('notas.txt', aluno)