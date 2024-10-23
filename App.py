from webbrowser import get
from Usuarios import Usuarios
from tkinter import * 
import mysql.connector

class Application:

    def __init__(self, master = None):
        self.font = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1 ["pady"] = 10
        self.container1.pack()

        self.container2 = Frame (master)
        self.container2 ["padx"] = 20 
        self.container2 ["pady"] = 5
        self.container2.pack()

        self.container3 = Frame (master)
        self.container3 ["padx"] = 20 
        self.container3 ["pady"] = 5
        self.container3.pack()
        
        self.container4 = Frame (master)
        self.container4 ["padx"] = 20 
        self.container4 ["pady"] = 5
        self.container4.pack()

        self.container5 = Frame (master)
        self.container5 ["padx"] = 20 
        self.container5 ["pady"] = 5
        self.container5.pack()

        self.container6 = Frame (master)
        self.container6 ["padx"] = 20 
        self.container6 ["pady"] = 5
        self.container6.pack()

        self.container7 = Frame (master)
        self.container7 ["padx"] = 20 
        self.container7 ["pady"] = 5
        self.container7.pack()

        self.container8 = Frame (master)
        self.container8 ["padx"] = 20 
        self.container8 ["pady"] = 10
        self.container8.pack()

        self.container9 = Frame (master)
        self.container9 ["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1,text="Informe os dados: ")
        self.titulo ["fonte"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidusuario = Label (self.container2, text="IdUsuario: ", font = self.fonte,width=10)
        self.lblidusuario.pack()
        self.txtidusuario = Entry (self.container2)
        self.txtidusuario ["width"]=10
        self.txtidusuario ["width"] = self.fonte
        self.txtidusuario.pack(side = LEFT)

        self.btnBuscar = Button(self.container3,text = "Buscar",font = self.fonte,width = 10)
        self.btnBuscar ["command"] = self.buscarUsuario
        self.btnBuscar.pack(side = RIGHT)

        self.lblnome = Label (self.container3, text="Nome: ", font = self.fonte, width=10)
        self.lblnome.pack()
        self.txtnome = Entry(self.container3)
        self.txtnome ["width"]=25
        self.txtnome ["width"] = self.fonte
        self.txtnome.pack(side = LEFT)

        self.lbltelefone = Label (self.container4, text="Telefone: ", font = self.fonte, width=10)
        self.lbltelefone.pack()
        self.txttelefone = Entry(self.container4)
        self.txttelefone ["width"]=25
        self.txttelefone ["width"] = self.fonte
        self.txttelefone.pack(side = LEFT)

        self.lblemail = Label (self.container5, text="Telefone: ", font = self.fonte, width=10)
        self.lblemail.pack()

        self.txtemail = Entry(self.container5)
        self.txtemail ["width"]=25
        self.txtemail ["width"] = self.fonte
        self.txtemail.pack(side = LEFT)

        self.lblusuario = Label(self.container6,text="Usuario: ",font=self.fonte,width=10)
        self.lblusuario.pack(side=LEFT)
        self.lblusuario = Entry(self.container6)
        self.lblusuario ["width"] = 25 
        self.lblusuario ["show"] = "*"
        self.lblusuario ["font"] = self.fonte
        self.lblusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7,text="Senha: ",font=self.fonte,width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container7)
        self.txtsenha ["width"] = 25 
        self.txtsenha ["show"] = "*"
        self.txtsenha ["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        self.btnInsert = Button(self.container8, text = "Inserir", font=self.fonte, width=12)
        self.btnInsert ["command"] = self.InserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.btnAlterar = Button(self.container8, text = "Alterar", font=self.fonte, width=12)
        self.btnAlterar ["command"] = self.AlterarUsuario
        self.btnAlterar.pack (side=LEFT)

        self.btnExcluir = Button(self.container8, text = "Excluir", font=self.fonte, width=12)
        self.btnExcluir ["command"] = self.ExluirUsuario
        self.btnExcluir.pack (side=LEFT)

        self.btnLimpar = Button(self.container8, text = "Limpar", font=self.fonte, width=12)
        self.btnLimpar ["command"] = self.LimparCampos
        self.btnLimpar.pack (side=LEFT)


        self.lblmsg = Label (self.container9, text = "") 
        self.lblmsg ["font"] = ("Verdana","9","italic")
        self.lblmsg.pack()

        self.conectarBanco()

    def conectarBanco(self):
        self.conn = mysql.conenector.connect(
        host = 'localhost',
    	user = 'root',
    	password = 'root',
    	database = 'nicolassantana_db'
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
            idUsuario INT AUTO INCREMENT PRIMARY KEY,
            nome VARCHAR (255),
            telefone VARCHAR (255),
            email VARCHAR (255),
            usuario VARCHAR (255),
            senha VARCHAR (255))''')
        self.conn.commit()
    def InserirUsuario(self):
        nome = self.txtnome.get()
        telefone = self.txttelefone.get()
        email = self.txtemail.get()
        usuario = self.txtusuario.get()
        senha = self.txtsenha.get()
        self.cursor.execute ("INSERT INTO usuario(nome, telefone, email, usuario, senha)VALUES(%s,%s,%s,%s,%s,)",
            (nome,telefone,email,usuario,senha))
        self.conn.commit()
        self.lblmsg ["text"] = "Usuario inserido com sucesso"
        self.LimparCampos
        
    def AlterarUsuario(self):
        nome = self.txtnome.get()
        telefone = self.txttelefone.get()
        email = self.txtemail.get()
        usuario = self.txtusuario.get()
        senha = self.txtsenha.get()
        self.cursor.execute ("UPDATE INTO usuario(nome, telefone, email, usuario, senha)VALUES(%s,%s,%s,%s,%s,)",
            (nome,telefone,email,usuario,senha))
        self.conn.commit()
        self.lblmsg ["text"] = "Usuario alterado com sucesso"
        self.LimparCampos

    def ExluirUsuario(self):
        id_usuario = self.txtidusuario.get()
        self.cursor.execute("DELETE FROM aluno WHERE idUsuario = %s",(id_usuario,))
        self.conn.commit()
        self.lblmsg["text"] = "Usuario Excluido com sucesso!"
        self.LimparCampos()

    def BuscarUsuario(self):
        id_usuario = self.txtidusuario.get
        self.cursor.execute("SELECT * FROM aluno WHERE idUsuario = %s",(id_usuario,))
        usuario = self.cursorfetchone()

        if usuario:
            self.txtnome.insert(0,usuario[1])
            self.txttelefone.insert(0,usuario[2])
            self.txtemail.insert(0,usuario[3])
            self.txtusuario.insert(0,usuario[4])
            self.txtsenha.insert(0,usuario[5])
        else:
            self.lblmsg["text"] = "Usuario nao encontrado!"
            self.LimparCampos()


    def LimparCampos(self):
            self.txtnome.delete(0, END)
            self.txttelefone.delete(0, END)
            self.txtemail.delete(0, END)
            self.txtusuario.delete(0, END)
            self.txtsenha.delete(0, END)

    def __del__(sel):
        self.conn.close()


if __name__=="__main__":
    root = Tk()
    Application(root) 
    root.mainloop()

