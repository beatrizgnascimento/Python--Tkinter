import tkinter as tk
from tkinter import messagebox


class Artista:

  def __init__(self, nome) -> None:
    self.__nome = nome
    self.__albuns = []
    self.__musicas = []

  @property
  def nome(self):
    return self.__nome

  @property
  def albuns(self):
    return self.__albuns

  @property
  def musicas(self):
    return self.__musicas


class CtrlArtista:

  def __init__(self) -> None:
    self.artistas = []
    self.LimiteCadastraArtista = None

  def mostraMesagem(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

  def getArtista(self, nome):
    for art in self.artistas:
      if art.nome == nome:
        return art

  def getMusica(self, nomeMusica, musicas):
    for mus in musicas:
      if mus.nome == nomeMusica:
        return mus

  def getMusicaLista(self, artista: Artista):
    return artista.musicas

  def cadastraArtista(self):
    self.LimiteCadastraArtista = LimiteCadastraArtista(self)

  def enterHandler(self, event):
    nome = self.LimiteCadastraArtista.inputNome.get()
    artista = self.getArtista(nome)
    if artista is None:
      artista = Artista(nome)
      self.artistas.append(artista)
      self.mostraMesagem('Cadastro de Artista',
                         'Artista cadastrado com sucesso!')

  def cancelaHandler(self, event):
    self.LimiteCadastraArtista.destroy()

  def clear(self):
    self.LimiteCadastraArtista.inputNome.delete(
        0, len(self.LimiteCadastraArtista.inputNome.get()))

  def consultaArtista(self):
    artistString = "Artistas: \n"

    for artist in self.artistas:
      artistString += f"  --- {artist.nome}:\n"
      for album in artist.albuns:
        artistString += f"       -> {album.titulo} ({album.ano}): \n"
        for musica in album.musicas:
          artistString += f"{musica.nome}\n"

    LimiteConsulta = LimiteConsultaArtista(artistString)


class LimiteCadastraArtista(tk.Toplevel):

  def __init__(self, controle: CtrlArtista) -> None:
    self.controle = controle
    tk.Toplevel.__init__(self)
    self.title("Cadastro de Artista")

    self.frameNome = tk.Frame(self)
    self.frameButton = tk.Frame(self)

    self.labelNome = tk.Label(self.frameNome, text="Nome: ")
    self.inputNome = tk.Entry(self.frameNome, width=20)

    self.labelNome.pack(side='left')
    self.inputNome.pack(side='left')

    self.enterButton = tk.Button(self.frameButton, text='Enter')
    self.cancelaButton = tk.Button(self.frameButton, text='Cancelar')
    self.enterButton.bind("<Button>", self.controle.enterHandler)
    self.cancelaButton.bind("<Button>", self.controle.cancelaHandler)
    self.frameNome.pack(side='left')
    self.frameButton.pack(side='left')
    self.enterButton.pack(side='left')
    self.cancelaButton.pack(side='left')

  def mostraMensagem(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class LimiteConsultaArtista():

  def __init__(self, str: str):
    messagebox.showinfo('Lista de artistas', str)
