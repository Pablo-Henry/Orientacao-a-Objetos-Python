class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} Min - {self._likes} Likes'

# catálogo de filmes
homem_aranha = Filme("Homem Aranha através do aranhaverso", 2023, 136)
avatar = Filme("Avatar", 2009, 160)

# quantidade de likes
homem_aranha.dar_like()
homem_aranha.dar_like()
homem_aranha.dar_like()
homem_aranha.dar_like()
avatar.dar_like()
avatar.dar_like()
avatar.dar_like()

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes'

# catálogo de séries
rick_and_morty = Serie("Rick and Morty", 2013, 6)
breaking_bad = Serie("Breaking Bad", 2008, 5)
# quantidade de likes
rick_and_morty.dar_like()
rick_and_morty.dar_like()
rick_and_morty.dar_like()
rick_and_morty.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()

class Playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    def __getitem__(self, item):
        return self._programa[item]

    def __len__(self):
        return len(self._programa)


filmes_e_series = [homem_aranha, rick_and_morty, avatar, breaking_bad]

playlist_fim_de_semana = Playlist("Maratona do Fim de Semana", filmes_e_series )

print(f'Quantidade de intes dentro da Playlist: {len(playlist_fim_de_semana)}')


for programa in playlist_fim_de_semana:
    print(programa)


