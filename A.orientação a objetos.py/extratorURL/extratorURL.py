import re

class ExtratorURL:
    def __init__(self, url):
        self.url = url

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(padrao_url)
        if not match:
            raise ValueError("A URL não é válida")

    def url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def valor_parametro(self, parametro_busca):
        indice_parametro = self.url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.url_parametros()[indice_valor:]
        else:
            valor = self.url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.url_parametros() + "\n" + "URL Base: " + self.url_base()

url = "https://bytebank.com/cambio?MoedaOrigem=real&moedaDestino=dolar&quantidade=100"
extrator_url = ExtratorURL(url)
print(f'Tamanho da URL: {len(extrator_url)}')

valor_quantidade = extrator_url.valor_parametro("quantidade")
print(valor_quantidade)

