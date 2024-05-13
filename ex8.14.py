class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")


class LivroFisico(Livro):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self.paginas = paginas

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Número de páginas: {self.paginas}")


livro_fisico = LivroFisico("Turma da Mônica", "Especial de Natal", 30)

livro_fisico.mostrar_dados()