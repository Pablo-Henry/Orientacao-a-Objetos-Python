class Musica:
    def __init__(self, nome, autor, duracao):
        self._nome = nome.title()
        self.autor = autor.title()
        self.duracao = duracao
        self._vizualizacao = 0

    @property
    def nome(self):
        return self._nome

    def views(self):
        self._vizualizacao += 1

    @property
    def vizualizacao(self):
        return self.vizualizacao

    def __str__(self):
        return f'{self._nome} - Autor/Banda: {self.autor} - {self.duracao} Min'

class Rock(Musica):
    def __init__(self, nome, autor, tempo):
        super().__init__(nome, autor, tempo)

    def __str__(self):
        return f'{self._nome} - Autor/Banda: {self.autor} - {self.duracao} Min - Visualizações: {self._vizualizacao} Milhões'

fade_to_black = Rock('Fade to Black', 'Metallica', 7)
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()
fade_to_black.views()

class Funk(Musica):
    def __init__(self, nome, autor, duracao):
        super().__init__(nome, autor, duracao)

    def __str__(self):
        return f'{self._nome} - Autor/Banda: {self.autor} - {self.duracao} Min - Visualizações: {self._vizualizacao} Milhões'

trofeu = Funk('troféu', 'Mc Kevin', 3)
trofeu.views()
trofeu.views()
trofeu.views()
trofeu.views()
trofeu.views()

class Trap(Musica):
    def __init__(self, nome, autor, duracao):
        super().__init__(nome, autor, duracao)

    def __str__(self):
        return f'{self._nome} - Autor/Banda: {self.autor} - {self.duracao} Min - Visualizações: {self._vizualizacao} Milhões'

kiss = Trap('Kiss', 'Mc Igu', 3.24)
kiss.views()
kiss.views()
kiss.views()

class Rap(Musica):
    def __init__(self, nome, autor, duracao):
        super().__init__(nome, autor, duracao)

    def __str__(self):
        return f'{self._nome} - Autor/Banda: {self.autor} - {self.duracao} Min - Visualizações: {self._vizualizacao} Milhões'

da_ponte_pra_ca = Rap('Da Ponte Pra Cá', 'Racionais MCs', 8.47)
da_ponte_pra_ca.views()
da_ponte_pra_ca.views()
da_ponte_pra_ca.views()
da_ponte_pra_ca.views()
da_ponte_pra_ca.views()
da_ponte_pra_ca.views()
da_ponte_pra_ca.views()
da_ponte_pra_ca.views()
da_ponte_pra_ca.views()
da_ponte_pra_ca.views()

class Sertanejo(Musica):
    def __init__(self, nome, autor, duracao):
        super().__init__(nome, autor, duracao)

    def __str__(self):
        return f'{self._nome} - Autor/Banda: {self.autor} - {self.duracao} Min - Visualizações: {self._vizualizacao} Milhões'

leao = Sertanejo('Leão', 'Marilia mendonça', 4.00)
leao.views()
leao.views()
leao.views()
leao.views()
leao.views()
leao.views()
leao.views()
leao.views()
leao.views()

class PlayMusic:
    def __init__(self, nome, musicas):
        self.nome = nome
        self._musicas = musicas

    def __getitem__(self, item):
        return self._musicas[item]

    def __len__(self):
        return len(self._musicas)

musicas = [fade_to_black, trofeu, kiss, leao, da_ponte_pra_ca]

tudo_misturado = PlayMusic('Tudo Misturado', musicas)

print(f'Quantidade de musicas: {len(tudo_misturado)}')

for songs in tudo_misturado:
    print(songs)

