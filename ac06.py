# Bryan de Almeida Gonçalves - RA: 1901236


class Funcionario:
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

    def get_cursos(self, curso):
        return self.__cursos


class Curso:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def exibir(self):
        print(self.codigo)
        print(self.nome)

    def get_nome(self):
        return self.nome


class Disciplina:
    def __init__(self, codigo, nome, carga_horaria, curso):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.curso = curso

    def get_carga_horaria(self):
        return self.carga_horaria

    def exibir(self):
        print(self.codigo)
        print(self.nome)
        print(self.carga_horaria)
        print(self.curso)


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.__disciplinas = []

    def incluir_disciplina(self, disciplina):
        if len(self.__disciplinas) == 5:
            raise ValueError
        else:
            self.__disciplinas.append(disciplina)

    def get_disciplinas(self):
        return self.__disciplinas


class Professor(Funcionario):
    def __init__(self, titulacao, area, codigo, nome, email,
                 telefone, cpf):
        self.titulacao = titulacao
        self.__disciplinas = []
        super().__init__(codigo, nome, email, telefone, cpf)

    def incluir_disciplina(self, disciplina):
        ch = 0
        for i in range(len(self.__disciplinas)):
            ch += disciplina.get_carga_horaria()

            if ch <= 200:
                self.__disciplinas.append(disciplina)
            else:
                raise ValueError

    def get_disciplinas(self):
        return self.__disciplinas
