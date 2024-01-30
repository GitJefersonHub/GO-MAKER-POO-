# Dicente: Jeferson Alves
# GO MAKER Univangélica
# DISCIPLINA "Programação Orientada a Objeto"
# Sistema de Gerenciamento de Bibliotecas
class Livro:
    def __init__(self, titulo, autor, ano, disponivel) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = bool(disponivel)

    def __str__(self) -> str:
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Disponivel: {self.disponivel}"

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

########################################################################################################################

class Revista(Livro):
    def __init__(self, titulo, autor, ano, disponivel, numero) -> None:
        super().__init__(titulo, autor, ano, disponivel)
        self.numero = numero

    def __str__(self) -> str:
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Disponivel: {self.disponivel}, Numero: {self.numero}"

########################################################################################################################

class Membro:
    def __init__(self, nome, id) -> None:
        self.nome = nome
        self.membro_id = id

    def __str__(self) -> str:
        return f"Nome: {self.nome}, ID: {self.membro_id}"

########################################################################################################################

class Biblioteca:
    def __init__(self, livros, membros) -> None:
        self.livros = list(livros) or []
        self.membros = list(membros) or []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
        print(f"Livro {livro.titulo} adicionado com sucesso")

    def adicionar_membro(self, membro: Membro):
        self.membros.append(membro)
        print(f"Membro {membro.membro_id} - {membro.nome} adicionado com sucesso")

    def emprestar_livro(self, livro: Livro, membro: Membro):
        if membro not in self.membros:
            raise Exception("Membro nao cadastrado")

        if livro not in self.livros:
            raise Exception("Livro nao cadastrado")

        if (livro.disponivel):
            livro.emprestar()
            print(f"Livro {livro.titulo} emprestado com sucesso para {membro.nome}")
        else:
            raise Exception("Livro nao disponivel")

    def devolver_livro(self, livro: Livro, membro: Membro):
        if membro not in self.membros:
            # validar se o membro está cadastrado
            raise Exception("Membro nao cadastrado")

        if livro not in self.livros:
            # validar se o livro está cadastrado
            raise Exception("Livro nao cadastrado")

        if (livro.disponivel):
            # validar se o livro está emprestado para o membro
            raise Exception("Livro ja disponivel")
        livro.devolver()
        print(f"Livro {livro.titulo} devolvido com sucesso por {membro.nome}")

    def listar_livros_emprestados(self) -> list[Livro]:
        # retorna lista de nomes dos livros que não estão disponiveis/ portanto emprestados
        return "Lista de livros emprestados: " + str([livro.titulo for livro in self.livros if not livro.disponivel])
def main():
    biblia = Livro("Biblia", "Deus", 0, True)
    revista_veja = Revista("Veja", "Editara Abril", 2021, True, 300)
    senhor_dos_aneis = Livro("Senhor dos Aneis", "J.R.R. Tolkien", 1954, True)

    jeferson = Membro("Jeferson", 1)
    professor = Membro("Professor", 2)

    biblioteca = Biblioteca([biblia, revista_veja], [jeferson])

    # tratamento de exceção para os comandos da biblioteca
    try:
        biblioteca.adicionar_livro(senhor_dos_aneis)
        biblioteca.adicionar_membro(professor)

        biblioteca.emprestar_livro(revista_veja, jeferson)
        print(biblioteca.listar_livros_emprestados())

        biblioteca.devolver_livro(revista_veja, jeferson)
        print(biblioteca.listar_livros_emprestados())

        biblioteca.devolver_livro(revista_veja, jeferson)
        print(biblioteca.listar_livros_emprestados())
    except Exception as e:
        print(e)
main()