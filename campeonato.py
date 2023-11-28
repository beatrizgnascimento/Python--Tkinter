import tkinter as tk
from tkinter import messagebox, ttk
import os.path
import pickle


class Curso:

  def __init__(self, sigla, nome) -> None:
    self.__sigla = sigla
    self.__nome = nome

  @property
  def sigla(self):
    return self.__sigla

  @property
  def nome(self):
    return self.__nome


class Estudante:

  def __init__(self, nroMatric, nome, curso) -> None:
    self.__nroMatric = nroMatric
    self.__nome = nome
    self.__curso = curso

  @property
  def nroMatric(self):
    return self.__nroMatric

  @property
  def nome(self):
    return self.__nome

  @property
  def curso(self):
    return self.__curso


class CtrlCampeonato:
  listaEstEquipe = [] # lista rascunho para que a equipe seja salva e depois seja trans para um dicionário
  def __init__(self) -> None:
    if not os.path.isfile("campeonato.pickle"):
      self.listaEquipe = []
    else:
      with open('campeonato.pickle', 'rb') as f:
        self.listaEquipe = pickle.load(f)

  c1 = Curso("CCO", "Ciência da Computação")
  c2 = Curso("SIN", "Sistemas de Informação")
  c3 = Curso("ECO", "Engenharia da Computação")
  listaCurso = [c1, c2, c3]
    #Inserir mais cursos, se quiser
  e1 = Estudante(1001, "José da Silva", c1)
  e2 = Estudante(1002, "João de Souza", c1)
  e3 = Estudante(1003, "Rui Santos", c2)
  e4 = Estudante(1004, "João Henrique", c2)
  e5 = Estudante(1005, "Carolina", c2)
  e6 = Estudante(1006, 'Pedro Lucas', c3)
  e7 = Estudante(1007, 'Flavio', c3)
  e8 = Estudante(1008, 'Beatriz', c2)
  e9 = Estudante(1010, "Iris", c1)
  e10 = Estudante(1011, 'Gabriel', c3)
  listaEstudante = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
    #Inserir mais 7 alunos, totalizando pelo menos 10 na lista

  def salvaEquipe(self):
    if len(self.listaEquipe) != 0:
      with open('campeonato.pickle', 'wb') as f:
        pickle.dump(self.listaEquipe, f)

  def getAluno(self, matricula, curso):
    for estudante in self.listaEstudante:
      if estudante.nroMatric == int(
          matricula) and estudante.curso.sigla == curso:
        return estudante
    #mensagem fora do loop 
    messagebox.showerror('Erro', 'Aluno não encontrado')
    return None

  def cadastrarAlunoHandler(self, event):
    curso_selecionado = self.LimiteCadastrarEquipe.selecaoCurso.get()
    matricula = self.LimiteCadastrarEquipe.inputMatricula.get()

    if matricula == '':
      messagebox.showerror('Erro', 'Preencha o campo matrícula')
      return

    aluno = self.getAluno(matricula, curso_selecionado)

    if aluno is not None:
      if aluno not in self.listaEstEquipe:
        self.listaEstEquipe.append(aluno)
        messagebox.showinfo('Sucesso', 'Aluno adicionado à equipe')
      else:
       messagebox.showwarning(
          'Aviso',
          'Aluno já está na equipe'
       )
    else:
      messagebox.showerror('Erro', 'Aluno não está matriculado no curso')

  def criarEquipeHandler(self, event):
    curso_selecionado = self.LimiteCadastrarEquipe.selecaoCurso.get()

    if len(self.listaEstEquipe) > 0:
      #chama um dicionário chamado equipe que contém o curso, a partir de uma lista de dicionários
      #listaEstudantes, chama o numero de matricula e nome
      equipe = {'curso': curso_selecionado, 'listaEstudantes': 
        [{
              'nroMatric': est.nroMatric,
              'nome': est.nome
          } for est in self.listaEstEquipe] #para cada estudante na lista do adicionar Aluno
      }
      if equipe not in self.listaEquipe:
        self.listaEquipe.append(equipe) #salva o dicionário na listaEquipe, que salva no arquivo
        self.salvaEquipe() #salva em arquivo
        messagebox.showinfo('Sucesso', 'Equipe criada com sucesso')
        self.listaEstEquipe = []  # Limpa a lista de estudantes da equipe
      else:
        messagebox.showwarning('Aviso', 'Equipe já existe')

  def consultarEquipeHandler(self, event):
    curso_consultado = self.LimiteConsultarEquipe.inputCurso.get()
    if curso_consultado == '':
      messagebox.showerror('Erro', 'Preencha este campo')

    curso_encontrado = False
    for curso in self.listaCurso:
        if curso.sigla == curso_consultado:
            curso_encontrado = True
            break

    if not curso_encontrado:
        messagebox.showerror('Erro', 'Esta sigla de curso não existe')
        return

    equipe_encontrada = False
    for equipe in self.listaEquipe:
        if equipe['curso'] == curso_consultado:
            print(f'Equipe do curso {curso_consultado}:')
            equipe_string = ''
            for estudante in equipe['listaEstudantes']:
                equipe_string += f'Nome: {estudante["nome"]}, Matrícula: {estudante["nroMatric"]}\n'
            equipe_encontrada = True

    if equipe_encontrada:
      self.mostraMensagem('Alunos', equipe_string)
    else:
        messagebox.showerror('Erro', 'Não existe equipe desse curso')


  def imprimirDadosHandler(self, event):
    num_equipes = len(self.listaEquipe)
    num_estudantes = 0
    media = 0
    msg = ''
    for equipe in self.listaEquipe:
      num_estudantes += len(equipe['listaEstudantes'])
      
    if num_equipes > 0:   
      media = num_estudantes / num_equipes
      msg += f'Número de equipes: {num_equipes}\nNúmero de estudantes: {num_estudantes}\nMédia: {media}\n' 
      self.mostraMensagem('Dados do campeonato', msg)
    else:
      self.mostraMensagem('Dados do campeonato', 'Não há equipes cadastradas')



  def mostraMensagem(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

  def cadastrarEquipe(self):
    self.LimiteCadastrarEquipe = LimiteCadastrarEquipe(self)

  def consultarEquipe(self):
    self.LimiteConsultarEquipe = LimiteConsultarEquipe(self)

 


class LimiteCadastrarEquipe(tk.Toplevel):

  def __init__(self, controle: CtrlCampeonato):
    self.controle = controle
    tk.Toplevel.__init__(self)
    self.title('Consultar equipe')

    self.frameCombo = tk.Frame(self)
    self.frameMatricula = tk.Frame(self)
    self.frameButton = tk.Frame(self)

    self.labelCombo = tk.Label(self.frameCombo, text='Curso: ')
    self.labelCombo.pack(side='left')
    self.selecaoCurso = tk.StringVar()
    self.comboCurso = ttk.Combobox(self.frameCombo,
                                   textvariable=self.selecaoCurso)
    self.comboCurso.pack(side='left')

    listaCursos = [curso.sigla for curso in self.controle.listaCurso]
    self.comboCurso.configure(values=listaCursos)

    self.labelMatricula = tk.Label(self.frameMatricula, text='Matrícula: ')
    self.labelMatricula.pack(side='left')
    self.inputMatricula = tk.Entry(self.frameMatricula)
    self.inputMatricula.pack(side='left')

    self.buttonCadastrar = tk.Button(self.frameButton,
                                     text='Adicionar à equipe')
    self.buttonCadastrar.pack(side='left')
    self.buttonCadastrar.bind("<ButtonRelease-1>",
                              self.controle.cadastrarAlunoHandler)

    self.buttonCriarEquipe = tk.Button(self.frameButton, text='Cria Equipe')
    self.buttonCriarEquipe.pack(side='left')
    self.buttonCriarEquipe.bind("<ButtonRelease-1>",
                                self.controle.criarEquipeHandler)

    self.frameMatricula.pack(side='left')
    self.frameCombo.pack(side='left')
    self.frameButton.pack(side='left')


class LimiteConsultarEquipe(tk.Toplevel):
  def __init__(self, controle: CtrlCampeonato):
    self.controle = controle
    tk.Toplevel.__init__(self)
    self.title('Consultar equipe')

    self.frameCurso = tk.Frame(self)
    self.frameButton = tk.Frame(self)

    self.labelCurso = tk.Label(self.frameCurso, text='Curso: ')
    self.labelCurso.pack(side='left')
    self.inputCurso = tk.Entry(self.frameCurso)
    self.inputCurso.pack(side='left')

    self.buttonBusca = tk.Button(self.frameButton, text='Buscar')
    self.buttonBusca.pack(side='left')
    self.buttonBusca.bind("<Button>", self.controle.consultarEquipeHandler)

    self.buttonImprimirDados = tk.Button(self.frameButton, text='Imprimir Dados')
    self.buttonImprimirDados.pack(side='left')
    self.buttonImprimirDados.bind("<ButtonRelease-1>", self.controle.imprimirDadosHandler)


    self.frameCurso.pack(side='left')
    self.frameButton.pack(side='left')





