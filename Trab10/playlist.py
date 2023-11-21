import tkinter as tk
from tkinter import ttk, messagebox


class Playlist:

  def __init__(self, nome, musicas: list) -> None:
    self.__nome = nome
    self.__musicas = musicas

  @property
  def nome(self):
    return self.__nome

  @property
  def musicas(self):
    return self.__musicas


class CtrlPlaylist:

  def __init__(self, ControlePrincipal) -> None:
    self.ControlePrincipal = ControlePrincipal
    self.listaPlaylist = []

  def mostraMensagem(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

  def sairBusca(self, event):
    self.LimiteConsultarPlaylist.destroy()

  def cadastrarPlaylist(self):
    self.musicas = []
    self.LimiteCadastrarPlaylist = LimiteCadastrarPlaylist(self)

  def consultarPlaylist(self):
    self.LimiteConsultarPlaylist = LimiteConsultarPlaylist(self)

  def getPlaylist(self, nome):
    for play in self.listaPlaylist:
      if play.nome == nome:
        return play

  def buscarArtista(self, event):
    self.LimiteCadastrarPlaylist.listaMusicas.delete(0, tk.END)
    nomeArtista = self.LimiteCadastrarPlaylist.selecaoArtista.get()
    artista = self.ControlePrincipal.ctrlArtista.getArtista(nomeArtista)
    self.musicasAtuais = self.ControlePrincipal.ctrlArtista.getMusicaLista(
        artista)
    for mus in self.musicasAtuais:
      if mus not in self.musicas:
       self.LimiteCadastrarPlaylist.listaMusicas.insert(tk.END, mus.nome)

  def registrarMusica(self, event):
    nomeMusicaSel = self.LimiteCadastrarPlaylist.listaMusicas.get(tk.ACTIVE)
    musicaSel = self.ControlePrincipal.ctrlArtista.getMusica(nomeMusicaSel, self.musicasAtuais)
    self.musicas.append(musicaSel)
    self.LimiteCadastrarPlaylist.listaMusicas.delete(tk.ACTIVE)
    self.mostraMensagem('Cadastro de Musica', 'Musica cadastrada com sucesso!')

  def registrarPlaylist(self, event):
    nomePlaylist = self.LimiteCadastrarPlaylist.inputPlaylistNome.get()
    listaMusicas = [musica for musica in self.musicas]
    self.listaPlaylist.append(Playlist(nomePlaylist, listaMusicas))
    self.clearHandler(event)
    self.mostraMensagem('Sucesso', 'Playlist cadastrada com sucesso')
    

  def consulta(self, event):
    nomePlaylist = self.LimiteConsultarPlaylist.SelecaoPlaylist.get()
    if nomePlaylist == '':
      return
    string = f"Faixas de {nomePlaylist}: \n"
    playlist = self.getPlaylist(nomePlaylist)
    for mus in playlist.musicas:
      string += f"{mus.nome}\n"
      
    self.mostraMensagem('Sucesso', string)
    

  def clear(self, *fields):
    for field in fields:
      field.delete(0, len(field.get()))

  def clearHandler(self, event):
    self.clear(self.LimiteCadastrarPlaylist.inputPlaylistNome,
               self.LimiteCadastrarPlaylist.selecaoArtista)
    self.LimiteCadastrarPlaylist.listaMusicas.delete(0, tk.END)

  def exitHandler(self, event):
    self.LimiteCadastrarPlaylist.destroy()


class LimiteCadastrarPlaylist(tk.Toplevel):

  def __init__(self, controle: CtrlPlaylist) -> None:
    self.controle = controle
    tk.Toplevel.__init__(self)
    self.title('Cadastro de Playlist')

    self.framePlaylist = tk.Frame(self)
    self.frameArtista = tk.Frame(self)
    self.frameMusica = tk.Frame(self)
    self.frameButton = tk.Frame(self)

    self.labelPlaylist= tk.Label(self.framePlaylist, text="Nome da playlist: ")
    self.inputPlaylistNome = tk.Entry(self.framePlaylist)

    self.inputPlaylistNome.pack(side="left")
    self.labelPlaylist.pack(side="left")
    

    self.labelArtista = tk.Label(self.frameArtista,
                                 text="Selecione o artista: ")
    self.artistaSelecionado = tk.StringVar()
    self.selecaoArtista = ttk.Combobox(self.frameArtista,
                                       textvariable=self.artistaSelecionado)
    listaArtista = [
        artista.nome for artista in self.controle.ControlePrincipal.ctrlArtista.artistas
    ]
    self.selecaoArtista.configure(values=listaArtista)

    self.labelArtista.pack(side='left')
    self.selecaoArtista.pack(side="left")

    self.listaMusicas = tk.Listbox(self.frameMusica)
    self.labelMusica = tk.Label(self.frameMusica, text='Músicas: ')
    self.buscaArtButton = tk.Button(self.frameButton, text='Procurar artista')
    self.salvarMusicaButton = tk.Button(self.frameButton, text="Salvar música")
    self.registrarPlaylistButton = tk.Button(self.frameButton,
                                             text="Salvar playlist")
    self.clearButton = tk.Button(self.frameButton, text="Limpar")

    self.buscaArtButton.bind("<Button>", self.controle.buscarArtista)
    self.salvarMusicaButton.bind("<Button>", self.controle.registrarMusica)
    self.registrarPlaylistButton.bind("<Button>",
                                      self.controle.registrarPlaylist)
    self.clearButton.bind("<Button>", self.controle.clearHandler)
    self.exitButton = tk.Button(self.frameButton, text="Sair")
    self.exitButton.bind("<Button>", self.controle.exitHandler)

    self.buscaArtButton.pack(side='top')
    self.salvarMusicaButton.pack(side='top')
    self.registrarPlaylistButton.pack(side='top')
    self.clearButton.pack(side='top')
    self.exitButton.pack(side='top')

    self.labelMusica.pack(side='top')
    self.listaMusicas.pack(side='left')
    
    self.framePlaylist.pack(side='top')
    self.frameArtista.pack(side='top')
    self.frameMusica.pack(side='left')
    self.frameButton.pack(side='top')



class LimiteConsultarPlaylist(tk.Toplevel):

  def __init__(self, controle: CtrlPlaylist) -> None:
    self.controle = controle
    tk.Toplevel.__init__(self)
    self.geometry('300x200')
    self.title('Consulta de Playlist')

    self.framePlaylist = tk.Frame(self)
    self.frameButton = tk.Frame(self)

    self.playlistSelecionada = tk.StringVar()
    self.SelecaoPlaylist = ttk.Combobox(self.framePlaylist,
                                        textvariable=self.playlistSelecionada)

    listaPlaylist = [playlist.nome for playlist in self.controle.listaPlaylist]

    self.SelecaoPlaylist.configure(values=listaPlaylist)
    self.labelPlaylist = tk.Label(self.framePlaylist,
                                  text="Selecione a playlist: ")
    self.labelPlaylist.pack(side='left')
    self.SelecaoPlaylist.pack(side="left")

    self.buscaButton = tk.Button(self.frameButton, text='Pesquisar')
    self.cancelaButton = tk.Button(self.frameButton, text='Cancelar')
    self.buscaButton.bind("<Button>", self.controle.consulta)
    self.cancelaButton.bind("<Button>", self.controle.sairBusca)

    self.buscaButton.pack(side='left')
    self.cancelaButton.pack(side='left')
    self.framePlaylist.pack(side='top')
    self.frameButton.pack(side='top')
