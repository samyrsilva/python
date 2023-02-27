#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
"""
        Tela de login com opção de entrar e de criar novo usuário, sendo que
    os usuários cadastrados são armazenados em um arquivo database.
"""
import shelve
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
except:
    print('Não foi possível importar o módulo tkinter')
    exit(1)

USUARIO_NAO_CADASTRADO = 1
SENHA_INVALIDA = 2
USUARIO_CADASTRADO_E_SENHA_CORRETA = 3
ERRO = 0
ARQUIVO = 'pessoas.db'
COR_DE_FUNDO = '#FFFFFF'
REMEMBER_USER_ATIVADO = 1
REMEMBER_USER_DESATIVADO = 0

class Pessoa(object):
    def __init__(self, user = '', password = '', nome = '', email = ''):
        self.user = user
        self.__password = password
        self.nome = nome
        self.email = email

class ArquivoDbm(object):
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def verifica_usuario(self, user = '', password = ''):
        """verifica se o usuário e senha, passados como argumentos, estão no arquivo dbm"""
        try:
            with shelve.open(self.arquivo) as p_db:
                if not user in p_db:
                    return USUARIO_NAO_CADASTRADO
                else:
                    if p_db[user][0] != password:
                        return SENHA_INVALIDA
                    else:
                        return USUARIO_CADASTRADO_E_SENHA_CORRETA
        except :
            print('Ocorreu um erro inesperado...')
            return ERRO

    def insere_usuario(self, user = '', password = '', nome = '', email = ''):
        """insere um novo usuário com sua senha, nome e e-mail no arquivo dbm"""
        try:
            with shelve.open(self.arquivo) as p_db:
                p_db[user] = [password, nome, email]
        except :
            print('Ocorreu um erro inesperado...')
            return ERRO

    def insere_ultimo_usuario_no_arq(self, ultimo_acesso = 'n', user = '', password = ''):
        """
        insere uma lista no arquivo dbm com o usuário e senha,
        e que representa o último acesso realizado. Caso o Check button
        esteja ativado
        """
        lista_de_ultimo_acesso = [ultimo_acesso, user, password]
        try:
            with shelve.open(self.arquivo) as p_db:
                p_db['ultimo_acesso'] = lista_de_ultimo_acesso
        except :
            print('Ocorreu um erro inesperado...1')
            exit(1)

    def devolve_ult_acesso(self):
        lista_de_ultimo_acesso = []
        try:
            with shelve.open(self.arquivo) as p_db:
                if 'ultimo_acesso' in p_db:
                    lista_de_ultimo_acesso = p_db['ultimo_acesso']
                    return lista_de_ultimo_acesso[0], lista_de_ultimo_acesso[1], lista_de_ultimo_acesso[2]
                else:
                    return 'n', '', ''
        except :
            print('Ocorreu um erro inesperado...2')
            exit(1)

class Login(object):
    def __init__(self, instancia):
        self.fonte = ('Trebuchet MS', '15') #, 'bold', 'underline', 'italic')

        self.arq_dbm = ArquivoDbm(ARQUIVO)
        self.pessoa = Pessoa()
        self.acessar_ult = ''   # Variável auxiliar que vai ler do arquivo dbm o caractere 's'(acessar último)
                                # ou 'n' (não acessar último user)
        self.lembrar_usuario = IntVar() # Variável auxiliar que alterará seu valor de acordo com o Check

        self.declara_widgets_signin(instancia)
        self.declara_widgets_createuser(instancia)

        self.sign_in()

    def declara_widget_checkbutton(self, master):
        self.remember_user = Checkbutton(master, text = 'Lembrar usuário', bg = COR_DE_FUNDO)
        self.remember_user['highlightbackground'] = COR_DE_FUNDO
        self.remember_user['activebackground'] = COR_DE_FUNDO
        self.remember_user['pady'] = 10
        self.remember_user['offvalue'] = REMEMBER_USER_DESATIVADO
        self.remember_user['onvalue'] = REMEMBER_USER_ATIVADO
        self.remember_user['variable'] = self.lembrar_usuario
        self.remember_user['highlightthickness'] = -1 # Retirando a borda ao redor do Checkbutton

    def declara_widgets_signin(self, instancia):
        """responsável por inicializar os frames"""
        # Frames da janela de sign in
        self.frame0 = Frame(instancia, bg = COR_DE_FUNDO)       # Frame da logo
        self.frame1 = Frame(instancia, bg = COR_DE_FUNDO)       # Frame do nome 'Usuário'
        self.frame2 = Frame(instancia, bg = COR_DE_FUNDO)       # Frame da entrada do user
        self.frame3 = Frame(instancia, bg = COR_DE_FUNDO)       # Frame do nome 'Senha'
        self.frame4 = Frame(instancia, bg = COR_DE_FUNDO)       # Frame da entrada de password
        self.frame5 = Frame(instancia, bg = COR_DE_FUNDO)       # Frame da info
        self.frame6 = Frame(instancia, bg = COR_DE_FUNDO)       # Frame do Check button
        self.frame7 = Frame(instancia, bg = COR_DE_FUNDO)       # Frame que contem a subframe dos buttons
        self.subframe0 = Frame(self.frame7, bg = COR_DE_FUNDO)  # Subframe que contém os buttons

        #Inserindo imagem de logo no programa
        logo = PhotoImage(file = 'images/logo2.gif')
        self.logo = Label(self.frame0)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo['bg'] = COR_DE_FUNDO

        #Texto que pede o nome de usuário
        self.user_signin = Label(self.frame1, text = 'Usuário', bg = COR_DE_FUNDO, font = self.fonte, fg = 'black')

        #Entrada do nome de usuário
        self.user_received_signin = Entry(self.frame2)

        #Texto de que pede a senha
        self.password_signin = Label(self.frame3, text = 'Senha', bg = COR_DE_FUNDO, font = self.fonte, fg = 'black')

        #Entrada da senha
        self.__password_received_signin = Entry(self.frame4, show = '*')

        #Texto com as informaçẽs de a respeito da validação do usuário
        self.info_signin = Label(self.frame5, text = '', pady = 10, bg = COR_DE_FUNDO, fg = 'red')

        #Chamando o CheckButton
        self.declara_widget_checkbutton(self.frame6)

        #Botões para entrar ou criar novo usuário
        self.enter_signin = Button(self.subframe0, text = 'ENTRAR', width = 7, command = self.__verificar)
        self.create_signin = Button(self.subframe0, text = 'NOVO', width = 7, bg = self.enter_signin['bg'], command = self.create_user)

    def inicializa_widgets_signin(self):
        self.frame0.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.subframe0.pack()

        self.logo.pack()
        self.user_signin.pack()
        self.user_received_signin.pack()
        self.password_signin.pack()
        self.__password_received_signin.pack()
        self.info_signin.pack()
        self.remember_user.pack()
        self.enter_signin.pack(side = 'left')
        self.create_signin.pack(side = 'right')

    def esquece_widgets_signin(self):
        self.frame0.pack_forget()
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.subframe0.pack_forget()

        self.logo.pack_forget()
        self.user_signin.pack_forget()
        self.user_received_signin.pack_forget()
        self.password_signin.pack_forget()
        self.__password_received_signin.pack_forget()
        self.info_signin.pack_forget()
        self.remember_user.pack_forget()
        self.enter_signin.pack_forget()
        self.create_signin.pack_forget()

    def destroi_widgets_signin(self):
        self.frame0.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.frame5.destroy()
        self.frame6.destroy()
        self.frame7.destroy()
        self.subframe0.destroy()

        self.logo.destroy()
        self.user_signin.destroy()
        self.user_received_signin.destroy()
        self.password_signin.destroy()
        self.__password_received_signin.destroy()
        self.info_signin.destroy()
        self.remember_user.destroy()
        self.enter_signin.destroy()
        self.create_signin.destroy()

    def declara_widgets_createuser(self, instancia):
        self.frame10 = Frame(instancia, bg = COR_DE_FUNDO)      # Frame do nome 'Nome'
        self.frame11 = Frame(instancia, bg = COR_DE_FUNDO)      # Frame da entrada do nome
        self.frame12 = Frame(instancia, bg = COR_DE_FUNDO)      # Frame do nome 'e-mail'
        self.frame13 = Frame(instancia, bg = COR_DE_FUNDO)      # Frame da entrada do e-mail
        self.frame14 = Frame(instancia, bg = COR_DE_FUNDO)      # Frame do nome 'Usuário'
        self.frame15 = Frame(instancia, bg = COR_DE_FUNDO)      # Frame da entrada do usuário
        self.frame16 = Frame(instancia, bg = COR_DE_FUNDO)      # Frame do nome 'Senha'
        self.frame17 = Frame(instancia, bg = COR_DE_FUNDO)      # Frame da entrada da senha
        self.frame18 = Frame(instancia, bg = COR_DE_FUNDO)      # Frame da info
        self.frame19 = Frame(instancia, bg = COR_DE_FUNDO)      # Frame da subframe dos buttons
        self.subframe1 = Frame(self.frame19, bg = COR_DE_FUNDO) # Subframe que contém os buttons

        #Texto que pede o nome
        self.nome_createuser = Label(self.frame10, text = 'Nome', bg = COR_DE_FUNDO, font = self.fonte, fg = 'green')

        #Entrada do nome
        self.nome_received_createuser = Entry(self.frame11, bg = COR_DE_FUNDO)

        #Texto que pede o e-mail
        self.email_createuser = Label(self.frame12, text = 'E-mail', bg = COR_DE_FUNDO, font = self.fonte, fg = 'green')

        #Entrada do e-mail
        self.email_received_createuser = Entry(self.frame13, bg = COR_DE_FUNDO)

        #Texto que pede o nome de usuário
        self.user_createuser_createuser = Label(self.frame14, text = 'Nome de usuário', bg = COR_DE_FUNDO, font = self.fonte, fg = 'green')

        #Entrada do nome de usuário
        self.user_received_createuser = Entry(self.frame15)

        #Texto de que pede a senha
        self.password_createuser = Label(self.frame16, text = 'Senha', bg = COR_DE_FUNDO, font = self.fonte, fg = 'green')

        #Entrada da senha
        self.__password_received_createuser = Entry(self.frame17, show = '*')

        #Texto com as informaçẽs de a respeito da validação do usuário
        self.info_createuser = Label(self.frame18, text = '', pady = 10, bg = COR_DE_FUNDO, fg = 'red')

        #Botões para entrar ou criar novo usuário
        self.enter_createuser = Button(self.subframe1, text = 'ENTRAR', width = 7, command = self.valida_antes_de_sign_in)
        self.create_createuser = Button(self.subframe1, text = 'CRIAR', width = 7, command = self.__inserir)
        self.create_createuser['fg'] = 'white'
        self.create_createuser['bg'] = 'black'

    def inicializa_widgets_createuser(self):
        self.frame10.pack()
        self.frame11.pack()
        self.frame12.pack()
        self.frame13.pack()
        self.frame14.pack()
        self.frame15.pack()
        self.frame16.pack()
        self.frame17.pack()
        self.frame18.pack()
        self.frame19.pack()
        self.subframe1.pack()

        self.nome_createuser.pack()
        self.nome_received_createuser.pack()
        self.email_createuser.pack()
        self.email_received_createuser.pack()
        self.user_createuser_createuser.pack()
        self.user_received_createuser.pack()
        self.password_createuser.pack()
        self.__password_received_createuser.pack()
        self.info_createuser.pack()
        self.remember_user.pack()
        self.enter_createuser.pack(side = 'left')
        self.create_createuser.pack(side = 'right')

    def esquece_widgets_createuser(self):
        self.frame10.pack_forget()
        self.frame11.pack_forget()
        self.frame12.pack_forget()
        self.frame13.pack_forget()
        self.frame14.pack_forget()
        self.frame15.pack_forget()
        self.frame16.pack_forget()
        self.frame17.pack_forget()
        self.frame18.pack_forget()
        self.frame19.pack_forget()
        self.subframe1.pack_forget()

        self.nome_createuser.pack_forget()
        self.nome_received_createuser.pack_forget()
        self.email_createuser.pack_forget()
        self.email_received_createuser.pack_forget()
        self.user_createuser_createuser.pack_forget()
        self.user_received_createuser.pack_forget()
        self.password_createuser.pack_forget()
        self.__password_received_createuser.pack_forget()
        self.info_createuser.pack_forget()
        self.remember_user.pack_forget()
        self.enter_createuser.pack_forget()
        self.create_createuser.pack_forget()

    def destroi_widgets_createuser(self):
        self.frame10.destroy()
        self.frame11.destroy()
        self.frame12.destroy()
        self.frame13.destroy()
        self.frame14.destroy()
        self.frame15.destroy()
        self.frame16.destroy()
        self.frame17.destroy()
        self.frame18.destroy()
        self.frame19.destroy()
        self.subframe1.destroy()

        self.nome_createuser.destroy()
        self.nome_received_createuser.destroy()
        self.email_createuser.destroy()
        self.email_received_createuser.destroy()
        self.user_createuser_createuser.destroy()
        self.user_received_createuser.destroy()
        self.password_createuser.destroy()
        self.__password_received_createuser.destroy()
        self.info_createuser.destroy()
        self.remember_user.destroy()
        self.enter_createuser.destroy()
        self.create_createuser.destroy()

    def valida_antes_de_sign_in(self):
        self.esquece_widgets_createuser()
        self.sign_in()

    def sign_in(self):
        self.inicializa_widgets_signin()

        self.user_received_signin.delete(0, END)
        self.__password_received_signin.delete(0, END)

        #Verifica se o último usuário que fez login desejou que lembrasse do nome de usuário e senha dela
        self.acessar_ult, self.pessoa.user, self.pessoa.__password = self.arq_dbm.devolve_ult_acesso()

        #Se tiver desejado que lembrasse então atribui suas informações aos widgets: user_received e password_reecived
        if self.lembrar_usuario.get() == REMEMBER_USER_ATIVADO or self.acessar_ult == 's':
            self.user_received_signin.insert(END, self.pessoa.user)
            self.__password_received_signin.insert(END, self.pessoa.__password)
            self.remember_user.select()

    def create_user(self):
        self.esquece_widgets_signin()
        self.inicializa_widgets_createuser()

    def __inserir(self):
        """Insere os dados no novo usuário, mas antes fazendo as devidas validações dos dados"""
        self.pessoa.nome = self.nome_received_createuser.get().lower()
        self.pessoa.email = self.email_received_createuser.get().lower()
        self.pessoa.user = self.user_received_createuser.get().lower()
        self.pessoa.__password = self.__password_received_createuser.get()

        if (self.pessoa.nome or self.pessoa.email or self.pessoa.user or self.pessoa.__password) == '' :
            self.info_createuser['text'] = 'Nenhum campo pode ficar em branco'
            self.info_createuser['fg'] = 'red'
        else:
            if self.arq_dbm.verifica_usuario(self.pessoa.user) == USUARIO_NAO_CADASTRADO:
                self.arq_dbm.insere_usuario(self.pessoa.user, self.pessoa.__password, self.pessoa.nome, self.pessoa.email)
                self.arq_dbm.insere_ultimo_usuario_no_arq('s', self.pessoa.user, self.pessoa.password)
                self.esquece_widgets_createuser()
                self.sign_in()
            else:
                self.info_createuser['text'] = 'Usuário já cadastrado'

    def __verificar(self):
        """Verifica se o nome de usuário e senha estão corretos e se deseja que lembre desses dados"""
        self.pessoa.user = self.user_received_signin.get().lower()
        self.pessoa.__password = self.__password_received_signin.get()

        #Valida suas informações de login no arquivo que os tem guardados

        if (self.pessoa.user or self.pessoa.__password) == '' :
            self.info_signin['text'] = 'Nenhum campo pode ficar em branco'
            self.info_signin['fg'] = 'red'
        else:
            resultado = self.arq_dbm.verifica_usuario(self.pessoa.user, self.pessoa.__password)
            if resultado == USUARIO_NAO_CADASTRADO:
                self.info_signin['text'] = 'Usuário não cadastrado'
            else:
                if resultado == SENHA_INVALIDA:
                    self.info_signin['text'] = 'Senha inválida'
                else:
                    if resultado == USUARIO_CADASTRADO_E_SENHA_CORRETA:
                        if self.lembrar_usuario.get() == REMEMBER_USER_ATIVADO:
                            self.arq_dbm.insere_ultimo_usuario_no_arq('s', self.pessoa.user, self.pessoa.__password)
                        else:
                            self.arq_dbm.insere_ultimo_usuario_no_arq('n')
                        self.destroi_widgets_createuser()
                        self.destroi_widgets_signin()
                    else:
                        if resultado == ERRO:
                            exit(1)

instancia = Tk()
instancia.title('Login')
instancia['bg'] = COR_DE_FUNDO
instancia.geometry('800x600')

Login(instancia)

instancia.mainloop()