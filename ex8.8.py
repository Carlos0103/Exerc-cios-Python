class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Matrícula: {self.matricula}")

aluno = Aluno("Nabucodonosor", 20, "20211SI099")
aluno.mostrar_dados()