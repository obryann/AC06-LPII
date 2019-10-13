class Funcionario():
    def __init__(self, codigo, nome, email, telefone, cpf):
        self.codigo = codigo
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf


class Coordenador(Funcionario):
    def __init__(self, codigo, nome, email, telefone, cpf):
        self.__cursos = []
        super().__init__(codigo, nome, email, telefone, cpf)

    def incluir_curso(self, curso):
        self.__cursos.append(curso)

    def get_curso(self, curso):
        return self.__cursos


class Curso():
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome


class Disciplina():
    def __init__(self, codigo, nome, carga_horaria, curso):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.curso = curso


class Aluno():
    def __init__(self, nome, disciplinas):
        self.nome = nome
        self.__disciplinas = disciplinas


class Professor(Funcionario):
    def __init__(self, titulacao, area, disciplinas, codigo, nome, email,
                 telefone, cpf):
        self.titulacao = titulacao
        self.__disciplinas = disciplinas
        super().__init__(codigo, nome, email, telefone, cpf)
