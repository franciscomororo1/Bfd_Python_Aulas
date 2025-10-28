class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def lerLivro(self, livro):
        print(f"{self.nome} terminou de ler o livro {livro.titulo}")

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

pessoa = Pessoa("Francisco")
livro = Livro("A Moreninha")
pessoa.lerLivro(livro)