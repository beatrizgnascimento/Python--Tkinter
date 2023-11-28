import tkinter as tk
from tkinter import messagebox
import campeonato as campeonato

class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.limite = LimitePrincipal(self.root, self)
        self.CtrlCampeonato= campeonato.CtrlCampeonato()

        self.root.mainloop()

    def cadastrarEquipe(self):
        self.CtrlCampeonato.cadastrarEquipe()

    def consultarEquipe(self):
        self.CtrlCampeonato.consultarEquipe()
    
    def imprimirDados(self):
      self.CtrlCampeonato.imprimirDados()

class LimitePrincipal:
    def __init__(self, root, controle: ControlePrincipal):
        self.root = root
        self.root.geometry("300x300")
        self.root.title("Título do aplicativo")
        self.controle = controle

        self.menubar = tk.Menu(self.root)
        self.campeonatoMenu = tk.Menu(self.menubar)

        self.menubar.add_cascade(label="Campeonato", menu=self.campeonatoMenu)
        self.campeonatoMenu.add_command(label="Cadastrar", \
                          command=self.controle.cadastrarEquipe)
        self.campeonatoMenu.add_command(label="Consultar", \
                          command=self.controle.consultarEquipe)

        self.root.config(menu=self.menubar)
        

if __name__ == '__main__':
  c = ControlePrincipal()
  