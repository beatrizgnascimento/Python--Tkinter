from artista import Artista


class Musica():

  def __init__(self, nome, artista: Artista, numMusica):
      self.__nome = nome
      self.__artista = artista
      self.__numMusica = numMusica
      self.__artista.musicas.append(self)

  @property
  def nome(self):
      return self.__nome

  @property
  def artista(self):
      return self.__artista

  @property
  def numMusica(self):
      return self.__numMusica
