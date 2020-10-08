class Node():
    def __init__(self, key, cor):
        self._p = None
        self._right = None
        self._key = key
        self._left = None
        self._cor = cor

    def get_cor(self):
        return self._cor

    def set_cor(self, valor):
        self._cor = valor

    def get_key(self):
        return self._key

    def set_key(self, value):
        self._key = value

    def get_right(self):
        return self._right

    def set_right(self, value):
        self._right = value

    def get_left(self):
        return self._left

    def set_left(self, value):
        self._left = value

    def get_p(self):
        return self._p

    def set_p(self, value):
        self._p = value


class ARB():
    def __init__(self):
        self.__nil = Node(None, "BLACK")
        self.__nil.set_left(self.get_nil())
        self.__nil.set_right(self.get_nil())
        self.__root = self.get_nil()

    def get_root(self):
        return self.__root

    def set_root(self, valor):
        self.__root = valor

    def get_nil(self):
        return self.__nil

    def set_nil(self, valor):
        self.__nil = valor

    def Altura(self, x):
        if x == self.get_nil():
            return -1
        h1 = self.Altura(x.get_left())
        h2 = self.Altura(x.get_right())
        return (1 + max(h1, h2))
    def Inorder(self, x):
        if x != self.get_nil():
            self.Inorder(x.get_left())
            print(x.get_key().get_id(),x.get_key().get_name()) #id(nome)
            self.Inorder(x.get_right())
    def SearchId(self, x, k):
        while x != self.get_nil() and k != x.get_key().get_id():
            if k < x.get_key().get_id():
                x = x.get_left()
            else:
                x = x.get_right()
        return x
    def SearchNome(self, x, k):
        while x != self.get_nil() and k != x.get_key().get_name():
            if k < x.get_key().get_name():
                x = x.get_left()
            else:
                x = x.get_right()
        return x

    def Minimo(self, x):
        while x.get_left() != self.get_nil():
            x = x.get_left()
        return x

    def Maximo(self, x):
        while x.get_right() != self.get_nil():
            x = x.get_right()
        return x

    def Sucessor(self, x):
        if x.get_right() != self.get_nil():
            return self.Minimo(x.get_right())
        else:
            y = x.get_p()
            while y != self.get_nil() and x == y.get_right():
                x = y
                y = y.get_p()
            return y

    def Predecessor(self, x):
        if x.get_left() != self.get_nil():
            return self.Maximo(x.get_left())
        else:
            y = x.get_p()
            while y != self.get_nil() and x == y.get_left():
                x = y
                y = y.get_p()
            return y
    def Insert_Fixup(self, z):
        while z.get_p().get_cor() == "RED":
            if z.get_p() == z.get_p().get_p().get_left():
                y = z.get_p().get_p().get_right()
                if y.get_cor() == "RED":
                    z.get_p().set_cor("BLACK")
                    y.set_cor("BLACK")
                    z.get_p().get_p().set_cor("RED")
                    z = z.get_p().get_p()
                else:
                    if z == z.get_p().get_right():
                        z = z.get_p()
                        self.Left_Rotate(z)
                    z.get_p().set_cor("BLACK")
                    z.get_p().get_p().set_cor("RED")
                    self.Right_Rotate(z.get_p().get_p())
            else:
                y = z.get_p().get_p().get_left()
                if y.get_cor() == "RED":
                    z.get_p().set_cor("BLACK")
                    y.set_cor("BLACK")
                    z.get_p().get_p().set_cor("RED")
                    z = z.get_p().get_p()
                else:
                    if z == z.get_p().get_left():
                        z = z.get_p()
                        self.Right_Rotate(z)
                    z.get_p().set_cor("BLACK")
                    z.get_p().get_p().set_cor("RED")
                    self.Left_Rotate(z.get_p().get_p())
        self.get_root().set_cor("BLACK")

    def Insert(self, dado):
        new = Node(dado, "RED")
        y = self.get_nil()
        x = self.get_root()
        while x != self.get_nil():
            y = x
            if new.get_key().get_id() < x.get_key().get_id(): #Comparação pelo ID
                x = x.get_left()
            else:
                x = x.get_right()
        new.set_p(y)
        if y == self.get_nil():
            self.set_root(new)
        elif new.get_key().get_id() < y.get_key().get_id():
            y.set_left(new)
        else:
            y.set_right(new)
        new.set_right(self.get_nil())
        new.set_left(self.get_nil())
        new.set_cor("RED")
        self.Insert_Fixup(new)
    def Delete_Fixup(self, x):
        while x != self.get_root() and x.get_cor() == "BLACK":
            if x == x.get_p().get_left():
                w = x.get_p().get_right()
                if w.get_cor() == "RED":
                    w.set_cor("BLACK")
                    x.get_p().set_cor("RED")
                    self.Left_Rotate(x.get_p())
                    w = x.get_p().get_right()
                if w.get_left().get_cor() == "BLACK" and w.get_right().get_cor() == "BLACK":
                    w.set_cor("RED")
                    x = x.get_p()
                else:
                    if w.get_right() == "BLACK":
                        w.get_left().set_cor("BLACK")
                        w.set_cor("RED")
                        self.Right_Rotate(w)
                        w = x.get_p().get_right()
                        w.set_cor(x.get_p().get_cor())
                        x.get_p.set_cor("BLACK")
                        w.get_right().set_cor("BLACK")
                        self.Left_Rotate(x.get_p())
                        x = self.get_root()
            else:
                w = x.get_p().get_left()
                if w.get_cor() == "RED":
                    w.set_cor("BLACK")
                    x.get_p().set_cor("RED")
                    self.Right_Rotate(x.get_p())
                    w = x.get_p().get_left()
                if w.get_right().get_cor() == "BLACK" and w.get_left().get_cor() == "BLACK":
                    w.set_cor("RED")
                    x = x.get_p()
                else:
                    if w.get_left() == "BLACK":
                        w.get_right().set_cor("BLACK")
                        w.set_cor("RED")
                        self.Left_Rotate(w)
                        w = x.get_p().get_left()
                        w.set_cor(x.get_p().get_cor())
                        x.get_p.set_cor("BLACK")
                        w.get_left().set_cor("BLACK")
                        self.Right_Rotate(x.get_p())
                        x = self.get_root()
        x.set_cor("BLACK")

    def Delete(self,ID):
        z = self.SearchId(self.get_root(), ID)
        if z == self.get_nil():
            return 0
        if z.get_left() == self.get_nil() or z.get_right() == self.get_nil():
            y = z
        else:
            y = self.Sucessor(z)
        if y.get_left() != self.get_nil():
            x = y.get_left()
        else:
            x = y.get_right()
        if x != self.get_nil():
            x.set_p(y.get_p())
        if y.get_p() == self.get_nil():
            self.set_root(x)
        elif y == y.get_p().get_left():
            y.get_p().set_left(x)
        else:
            y.get_p().set_right(x)
        if y != z:
            z.set_key(y.get_key())
        if y.get_cor() == "BLACK":
            self.Delete_Fixup(x)
        return y

    def Left_Rotate(self, x):
        y = x.get_right()  # define y
        x.set_right(y.get_left())  # transforma a subárvore à esquerda y na subárvore à direita de x
        y.get_left().set_p(x)
        y.set_p(x.get_p())
        if x.get_p() == self.get_nil():  # In the RBT "None" is T.get_None()
            y.get_left().set_p(x)
        y.set_p(x.get_p())  # liga o pai de x a y
        if x.get_p() == self.get_nil():
            self.set_root(y)
        elif x == x.get_p().get_left():
            x.get_p().set_left(y)
        else:
            x.get_p().set_right(y)
        y.set_left(x)  # Coloca x à esquerda de y
        x.set_p(y)
      
    def Right_Rotate(self, x):
        y = x.get_left()
        x.set_left(y.get_right())
        y.get_right().set_p(x)
        y.set_p(x.get_p())
        if x.get_p() == self.get_nil():
            y.get_right().set_p(x)
        y.set_p(x.get_p())
        if x.get_p() == self.get_nil():
            self.set_root(y)
        elif x == x.get_p().get_right():
            x.get_p().set_right(y)
        else:
            x.get_p().set_left(y)
        y.set_right(x)
        x.set_p(y)
class Livro():
    num = 0
    def __init__(self,name):
        Livro.num += 1
        self.__id = Livro.num
        self.__name = name
        self.__status = True
    def get_id(self):
        return self.__id
    def set_id(self,valor):
        self.__id = valor
    def get_name(self):
        return self.__name
    def get_status(self):
        return self.__status
    def set_status(self,new):
        self.__status = new
class User():
  num = 0
  def __init__(self,name):
    User.num +=1
    self.__idUser = User.num
    self.__userName = name
    self.__listaID = []
    self.__listaLivros = []
    self.__qntEmprestimo = 0
  def get_livrosID(self):
    return self.__listaID
  def set_livrosID(self, ID):
    self.__listaID.append(ID)
  def removeID(self, ID):
    self.__listaID.remove(ID)
  def get_id(self):
    return self.__idUser
  def set_id(self,novoID):
    self.__idUser = novoID
  def get_name(self):
    return self.__userName
  def set_name(self, novoNome):
    self.__userName = novoNome
  def get_livros(self):
    return self.__listaLivros
  def addLivro(self, livro):
    self.__listaLivros.append(livro)
  def removeLivro(self, livro):
    self.__listaLivros.remove(livro)
  def getQnt(self):
    return self.__qntEmprestimo
  def setQnt(self):
    self.__qntEmprestimo +=1
  def subtraiQnt(self):
    self.__qntEmprestimo -=1
arcevoLivros = ARB()
listaUsuarios = ARB()
while True:
  print("-----------------------------------------------")
  print("Bem-vindo a Biblioteca BSI"),
  print("Escolha uma das opções abaixo:")
  print("1 - Cadastrar livro")
  print("2 - Descadastrar Livro")
  print("3 - Cadastrar Usuário")
  print("4 - Descadastrar Usuário")
  print("5 - Socilitar livro por empréstimo")
  print("6 - Devolver livro")
  print("7 - Apresentar relatórios")
  print("8 - Buscar livro")
  print("9 - Ver todos os livros do acervo")
  print("-----------------------------------------------")
  try:
   comando = int(input("Operação a realizar: "))
   if comando > 9 or comando <= 0:
     print("Digite uma opção válida")
  except:
    print("Digite uma opção válida")
  if comando == 1:
    cadastrarLivro = input("Digite o nome do livro: ")
    if cadastrarLivro == "":
      print("O nome não pode ser vazio")
    else:
      livro = Livro(cadastrarLivro)
      arcevoLivros.Insert(livro)
      print("Livro cadastrado com sucesso")
  elif comando == 2:
    print("------------------------------------------")
    print("Livros disponíveis no momento: ")
    arcevoLivros.Inorder(arcevoLivros.get_root())
    removerLivro = int(input("Digite o número de ID: "))
    x = arcevoLivros.SearchId(arcevoLivros.get_root(), removerLivro)
    x = x.get_key()
    if x == None:
      print("-------------------------------------------")
      print("Você tentou remover um livro que não existe")
    else:
      if x.get_status():
        arcevoLivros.Delete(removerLivro)
        print("Livro removido com sucesso")
      else:
        print("O livro está emprestado e não poderá ser removido")
  elif comando == 3:
    cadastrarUsuario = input("Digite o nome do usuário: ")
    if cadastrarUsuario == "":
      print("O nome não pode ser vazio")
    else:
      usuario = User(cadastrarUsuario)
      listaUsuarios.Insert(usuario)
      print("Usuário cadastrado com sucesso")
      print("Seu ID de usuário é: %d" % usuario.get_id())
  elif comando == 4:
    print("Usuários cadastrados no sistema:")
    listaUsuarios.Inorder(listaUsuarios.get_root())
    removerUsuario = int(input("Digite a ID do usuário:"))
    y = listaUsuarios.SearchId(listaUsuarios.get_root(),removerUsuario)
    y = y.get_key()
    if y == None:
      print("---------------------------------------------")
      print("Você tentou remover um usuário que não existe")
    else:
      if len(y.get_livros()) > 0:
        print("O usuário possui livros e não poderá ser deletado")
      else:
        listaUsuarios.Delete(removerUsuario)
        print("Usuário removido com sucesso")
  elif comando == 5:
    while True:
      userID = int(input("Digite seu ID de usuário: "))
      livroID = int(input("Digite o ID do Livro: "))
      idusuario = listaUsuarios.SearchId(listaUsuarios.get_root(),userID).get_key()
      idlivro = arcevoLivros.SearchId(arcevoLivros.get_root(), livroID).get_key()
      if idusuario == None or idlivro == None:
        print("-----------------------------------------------")
        print("Você digitou um ID de usuário ou livro inválido")
        break
      else:
        break
    while True:
      if idusuario != None and idlivro != None:
        if idlivro.get_status() == False:
          print("----------------------------------------------")
          print("Livro indisponível")
          break
        else:
          if idusuario.getQnt() <3:
            idusuario.setQnt()
            idlivro.set_status(False)
            idusuario.addLivro(idlivro.get_name())
            idusuario.set_livrosID(idlivro.get_id())
            print("O livro %s foi entregue ao usuário %s"% (idlivro.get_name(),idusuario.get_name()))
            break
          else:
            print("-------------------------------------------")
            print("O usuário excedeu o limite de empréstimos")
            break
      else:
        break
  elif comando == 6:
    verificador = 0
    verificadorUser = 0
    while True:
      userID = int(input("Digite seu número de usuário: "))
      idusuario = listaUsuarios.SearchId(listaUsuarios.get_root(),userID).get_key()
      if idusuario == None:
        print("----------------------------------------------")
        print("Você inseriu um ID de usuário inválido")
        verificadorUser +=1
        break
      if len(idusuario.get_livros()) == 0:
        print("----------------------------------------------")
        print("Você não pegou nenhum livro por empréstimo")
        verificador +=1
        break
      else:
        print("----------------------------------------------")
        print("Esses são os livros que você pegou: ")
        for i in range(len(idusuario.get_livros())):
          print("%d-%s"%(idusuario.get_livrosID()[i],idusuario.get_livros()[i]))
        devolverLivro = int(input("Digite o ID do livro que deseja devolver: "))
        livro = arcevoLivros.SearchId(arcevoLivros.get_root(), devolverLivro).get_key()
        if idusuario != None and livro != None:
          print("Livro {} devolvido com sucesso.".format(livro.get_name()))
          break
        else:
          print("----------------------------------------------")
          print("Número de usuário ou livro inválido")
          verificador +=1
          break
    if verificadorUser == 0 and verificador == 0:
      if livro.get_name() in idusuario.get_livros():
        livro.set_status(True)
        idusuario.subtraiQnt()
        idusuario.removeLivro(livro.get_name())
        idusuario.removeID(devolverLivro)
      else:
        print("------------------------------------------------")
        break
  elif comando == 7:
    entrada = input("Deseja ver o relatório por livro ou por usuário?: ")
    if entrada == "livro":
      idlivro = int(input("Insira a ID do livro: "))
      livro = arcevoLivros.SearchId(arcevoLivros.get_root(), idlivro).get_key()
      if livro != None:
        if livro.get_status() is True:
          print("O livro está disponível para empréstimo")
        else:
          print("O livro está emprestado")
      else:
        print("Este livro não existe")
    elif entrada == "usuário":
      iduser = int(input("Insira o ID do usuário:"))
      user = listaUsuarios.SearchId(listaUsuarios.get_root(), iduser).get_key()
      if user != None:
        if len(user.get_livros()) > 0:
          print("O usuário pegou os seguintes livros: ")
          for x in user.get_livros():
            print(x)
        else:
          print("O usuário não pegou nenhum livro por empréstimo")
    else:
      print("Você selecionou uma opção inválida")
  elif comando == 8:
    buscarLivro = input("Digite o nome do livro: ")
    z= arcevoLivros.SearchNome(arcevoLivros.get_root(), buscarLivro)
    z = z.get_key()
    if z == None:
      print("O livro não consta em nosso acervo")
    else:
      print("O livro consta no nosso acervo")
  elif comando == 9:
    print("Livros que possuímos atualmente:")
    arcevoLivros.Inorder(arcevoLivros.get_root())
