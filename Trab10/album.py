import tkinter as tk
from tkinter import messagebox, ttk
from artista import Artista
from musica import Musica


class Album:

  def __init__(self, titulo, ano, artista: Artista) -> None:
    self.__titulo = titulo
    self.__ano = ano
    self.__artista = artista
    self.__musicas = []

    self.__artista.albuns.append(self)

  @property
  def titulo(self):
    return self.__titulo

  @property
  def ano(self):
    return self.__ano

  @property
  def artista(self):
    return self.__artista

  @property
  def musicas(self):
    return self.__musicas


class CtrlAlbum:

  def __init__(self, ControlePrincipal) -> None:
    self.ControlePrincipal = ControlePrincipal
    self.listaAlbuns = []
    self.listaMusicas = []

  def mostraMensagem(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

  def cadastraAlbum(self):
    self.LimiteCadastraAlbum = LimiteCadastraAlbum(self)

  def consultaAlbum(self):
    self.LimiteConsultaAlbum = LimiteConsultaAlbum(self)

  def getAlbum(self, nome):
    for alb in self.listaAlbuns:
      if alb.titulo == nome:
        return alb

  def clear(self, *fields):
      for field in fields:
        field.delete(0, len(field.get()))

  def registrarMusicaHandler(self, event):
    if(self.LimiteCadastraAlbum.inputAlbum.get() == "" or 
       self.LimiteCadastraAlbum.inputAno.get() == "" or
       self.LimiteCadastraAlbum.selecaoArtista.get() == ""):
          return
    nomeMusica = self.LimiteCadastraAlbum.inputMusica.get()
    if nomeMusica == "":
        return 
    
    self.listaMusicas.append(nomeMusica)
    self.clear(self.LimiteCadastraAlbum.inputMusica)
    self.mostraMensagem('Sucesso', 'Música cadastrada com sucesso')
    self.LimiteCadastraAlbum.inputMusica.focus_force()

  def cadastrarAlbumHandler(self, event):
    nomeAlbum = self.LimiteCadastraAlbum.inputAlbum.get()
    nomeArtista = self.LimiteCadastraAlbum.artistaSelecionado.get()
    anoAlbum = self.LimiteCadastraAlbum.inputAno.get()
    if nomeAlbum == "" or nomeArtista == "" or anoAlbum == "": 
      return

    artista = self.ControlePrincipal.ctrlArtista.getArtista(nomeArtista)
    album = Album(nomeAlbum, anoAlbum, artista)

    for num, musica in enumerate(self.listaMusicas):
        album.musicas.append(Musica(musica, artista, num + 1))

    self.listaMusicas.clear()
    self.listaAlbuns.append(album)
    self.clearHandler(event)
    self.mostraMensagem('Sucesso', 'Album cadastrado com sucesso')
    self.LimiteCadastraAlbum.inputAlbum.focus_force()

  def clearHandler(self, event):
    self.clear(self.LimiteCadastraAlbum.inputAlbum,
               self.LimiteCadastraAlbum.inputMusica,
               self.LimiteCadastraAlbum.selecaoArtista,
               self.LimiteCadastraAlbum.inputAno)

  def buscaAlbum(self, event):
    nomeAlbum = self.LimiteConsultaAlbum.selecaoAlbum.get()
    album = self.getAlbum(nomeAlbum)
    string = f"Faixas de {album.titulo}: \n"

    for musica in album.musicas:
            string += f"{musica.nome}\n"

    self.mostraMensagem('Consulta de Album', string)
    
  def exitHandler(self, event):
    self.LimiteCadastraAlbum.destroy()
    
  def exitBusca(self, event):
    self.LimiteConsultaAlbum.destroy()


class LimiteCadastraAlbum(tk.Toplevel):

  def __init__(self, controle: CtrlAlbum) -> None:
    self.controle = controle
    tk.Toplevel.__init__(self)
    self.title('Registro de Album')

    self.frameAlbum = tk.Frame(self)
    self.frameArtista = tk.Frame(self)
    self.frameMusica = tk.Frame(self)
    self.frameButton = tk.Frame(self)

    self.artistaSelecionado = tk.StringVar()
    self.selecaoArtista = ttk.Combobox(self.frameArtista,
                                       textvariable=self.artistaSelecionado)

    listaArtistas = [
        artista.nome
        for artista in controle.ControlePrincipal.ctrlArtista.artistas
    ]

    self.selecaoArtista.configure(values=listaArtistas)

    self.labelArtista = tk.Label(self.frameArtista, text='Artista: ')
    self.labelArtista.pack(side='left')
    self.selecaoArtista.pack(side='left')

    self.labelMusica = tk.Label(self.frameMusica, text='Música')
    self.labelMusica.pack(side='left')
    self.inputMusica = tk.Entry(self.frameMusica)
    self.inputMusica.pack(side='left')

    self.labelAlbum = tk.Label(self.frameAlbum,
                               text='Digite o nome do Album: ')
    self.labelAno = tk.Label(self.frameAlbum, text='Ano de lançamento')
    self.inputAno = tk.Entry(self.frameAlbum)
    self.inputAlbum = tk.Entry(self.frameAlbum)

    self.inputAno.pack(side='right')
    self.labelAno.pack(side='right')
    self.labelAlbum.pack(side='left')
    self.inputAlbum.pack(side='left')
    
    self.buttonRegistrarMusica = tk.Button(self.frameButton,
                                           text='Salvar música')
    self.buttonRegistrarMusica.pack(side='left')
    \
    self.buttonRegistrarAlbum = tk.Button(self.frameButton,
                                          text='Salvar album')
    self.buttonRegistrarAlbum.pack(side='left')
    
    self.buttonCancelar = tk.Button(self.frameButton, text='Limpar')

    self.buttonRegistrarMusica.bind("<Button>",
                                    self.controle.registrarMusicaHandler)
    self.buttonRegistrarAlbum.bind("<Button>",
                                   self.controle.cadastrarAlbumHandler)
    self.buttonCancelar.bind("<Button>", self.controle.clearHandler)

    self.frameButton.pack(side='bottom')
    self.buttonCancelar.pack(side='left')
    self.frameAlbum.pack(side='top')
    self.frameArtista.pack(side='left')
    self.frameMusica.pack(side='bottom')


class LimiteConsultaAlbum(tk.Toplevel):

  def __init__(self, controle: CtrlAlbum):
    self.controle = controle
    tk.Toplevel.__init__(self)
    self.title('Consulta de Album')

    self.frameAlbum = tk.Frame(self)
    self.frameButton = tk.Frame(self)

    self.albumSelecionado = tk.StringVar()
    self.selecaoAlbum = ttk.Combobox(self.frameAlbum,
                                     textvariable=self.albumSelecionado)

    listaAlbums = [album.titulo for album in self.controle.listaAlbuns]

    self.selecaoAlbum.configure(values=listaAlbums)

    self.labelAlbum = tk.Label(self.frameAlbum, text='Selecione o album: ')
    self.labelAlbum.pack(side='left')
    self.selecaoAlbum.pack(side='left')

    self.buttonConsultarAlbum = tk.Button(self.frameButton, text='Consultar')
    self.buttonConsultarAlbum.bind("<Button>", self.controle.buscaAlbum)
    self.buttonConsultarAlbum.pack(side='left')
    self.buttonCancelar = tk.Button(self.frameButton, text='Cancelar')
    self.buttonCancelar.bind("<Button>", self.controle.exitBusca)
    self.buttonCancelar.pack(side='left')
    self.frameAlbum.pack(side='left')
    self.frameButton.pack(side='left')
