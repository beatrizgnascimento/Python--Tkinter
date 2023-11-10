import tkinter as tk
from tkinter import messagebox

class LimitePrincipal():
    def __init__(self, root, controle):
      self.controle = controle
      self.root = root
      self.root.geometry('300x250')
      self.menubar = tk.Menu(self.root)        
      self.artistaMenu = tk.Menu(self.menubar)
      self.albumMenu = tk.Menu(self.menubar)
      self.playlistMenu = tk.Menu(self.menubar)     

      self.artistaMenu.add_command(label="Insere", \
                  command=self.controle.insereEstudantes)
      self.artistaMenu.add_command(label="Mostra", \
                  command=self.controle.mostraEstudantes)
      self.menubar.add_cascade(label="Estudante", \
                  menu=self.artistaMenu)

      self.albumMenu.add_command(label="Insere", \
                  command=self.controle.insereDisciplinas)
      self.albumMenu.add_command(label="Mostra", \
                  command=self.controle.mostraDisciplinas)        
      self.menubar.add_cascade(label="Disciplina", \
                  menu=self.albumMenu)

      self.playlistMenu.add_command(label="Insere", \
                  command=self.controle.insereTurmas) 
      self.playlistMenu.add_command(label="Mostra", \
                  command=self.controle.mostraTurmas)                   
      self.menubar.add_cascade(label="Turma", \
                  menu=self.playlistMenu)        

      self.root.config(menu=self.menubar)

      
      