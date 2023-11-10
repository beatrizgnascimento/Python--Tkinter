import tkinter as tk
from tkinter import messagebox
import artista as art
import album as alb
import playlist as play


class LimitePrincipal():

  def __init__(self, root, controle):
    self.controle = controle
    self.root = root
    self.root.geometry('300x250')
    self.menubar = tk.Menu(self.root)
    self.artistaMenu = tk.Menu(self.menubar)
    self.albumMenu = tk.Menu(self.menubar)
    self.playlistMenu = tk.Menu(self.menubar)

    self.artistaMenu.add_command(label="Cadastrar", \
                command=self.controle.insereEstudantes)
    self.artistaMenu.add_command(label="Consultar", \
                command=self.controle.mostraEstudantes)
    self.menubar.add_cascade(label="Artista", \
                menu=self.artistaMenu)

    self.albumMenu.add_command(label="Cadastrar", \
                command=self.controle.insereDisciplinas)
    self.albumMenu.add_command(label="Consultar", \
                command=self.controle.mostraDisciplinas)
    self.menubar.add_cascade(label="Album", \
                menu=self.albumMenu)

    self.playlistMenu.add_command(label="Cadastrar", \
                command=self.controle.insereTurmas)
    self.playlistMenu.add_command(label="Consultar", \
                command=self.controle.mostraTurmas)
    self.menubar.add_cascade(label="Playlist", \
                menu=self.playlistMenu)

    self.root.config(menu=self.menubar)


class ControlePrincipal():

  def __init__(self) -> None:
    self.root = tk.Tk()

    self.ctrlArtista = art.CtrlArtista()
    self.ctrlAlbum = alb.CtrlAlbum()
    self.ctrlPlaylist = play.CtrlPlaylist()

    self.limite = LimitePrincipal(self.root, self)
    self.root.title("Playlist MVC")
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
    self.ctrlPlaylist.cadastraPlaylist()

  def consultaPlaylist(self):
    self.ctrlPlaylist.consultaPlaylist()


if __name__ == '__main__':
  c = ControlePrincipal()
