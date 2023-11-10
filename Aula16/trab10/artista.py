import tkinter as tk
from tkinter import messagebox

class Artista:
  def __init__(self, nome, album) -> None:
    self.__nome = nome 
    self.__album = album

  @property
  def nome(self):
    return self.__nome

  @property
  def album(self):
    return self.__album

class LimiteCadastraArtista(tk.Toplevel):
  def __init__(self, controle, listaAlbum) -> None:
    tk.Toplevel.__init__(self)
    self.geometry("250x100")
    self.title("Cadastro de Artista")
    self.controle = controle

    self.frameNome = tk.Frame(self)
    self.frameNome.pack()
    self.labelNome = tk.Label(self.frameNome, text="Nome: ")
    self.labelNome.pack(side="left")
    self.inputNome = tk.Entry(self.frameNome)
    self.inputNome.pack(side="left")

    self.frameButton = tk.Frame(self)
    self.frameButton.pack()
    self.buttonSubmit = tk.Button(self.frameButton,text="Enter")
    
