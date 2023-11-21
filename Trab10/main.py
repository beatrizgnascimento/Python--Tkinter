import tkinter as tk
from tkinter import messagebox
import artista as art
import album as alb
import playlist as play


class ControlePrincipal():

  def __init__(self) -> None:
    self.root = tk.Tk()

    self.ctrlArtista = art.CtrlArtista()
    self.ctrlAlbum = alb.CtrlAlbum(self)
    self.ctrlPlaylist = play.CtrlPlaylist(self)

    self.limite = LimitePrincipal(self.root, self)
    self.root.title("Sistema de Gestão de Música")
    self.root.geometry("500x500")
    self.root.mainloop()

  def cadastraArtista(self):
    self.ctrlArtista.cadastraArtista()

  def consultaArtista(self):
    self.ctrlArtista.consultaArtista()

  def cadastraAlbum(self):
    self.ctrlAlbum.cadastraAlbum()

  def consultaAlbum(self):
    self.ctrlAlbum.consultaAlbum()

  def cadastraPlaylist(self):
    self.ctrlPlaylist.cadastrarPlaylist()

  def consultaPlaylist(self):
    self.ctrlPlaylist.consultarPlaylist()


class LimitePrincipal():

  def __init__(self, root: tk.Tk, controle: ControlePrincipal):
    self.controle = controle
    self.root = root

    self.menubar = tk.Menu(self.root)
    self.artistaMenu = tk.Menu(self.menubar)
    self.albumMenu = tk.Menu(self.menubar)
    self.playlistMenu = tk.Menu(self.menubar)

    self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)
    self.menubar.add_cascade(label="Album", menu=self.albumMenu)
    self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)

    self.artistaMenu.add_command(label="Cadastrar",
                                 command=self.controle.cadastraArtista)
    self.artistaMenu.add_command(label="Mostrar",
                                 command=self.controle.consultaArtista)
    self.albumMenu.add_command(label="Cadastrar",
                               command=self.controle.cadastraAlbum)
    self.albumMenu.add_command(label="Mostrar",
                               command=self.controle.consultaAlbum)
    self.playlistMenu.add_command(label="Cadastrar",
                                  command=self.controle.cadastraPlaylist)
    self.playlistMenu.add_command(label="Mostrar",
                                  command=self.controle.consultaPlaylist)

    self.root.config(menu=self.menubar)


if __name__ == '__main__':
  c = ControlePrincipal()

