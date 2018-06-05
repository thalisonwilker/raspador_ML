from requests import get
from bs4 import BeautifulSoup

class Raspador(object):
	url = 'https://produto.mercadolivre.com.br/MLB-962858924-kit-bolsa-lorena-schutz-com-carteira-feminina-frete-gratis-_JM'

	def get(self):
		resp = get(self.url)
		if (resp.status_code == 200):
			Produto_ML(resp.text)

class  Produto_ML(object):
	__sopa = ''
	titulo = ''
	preco = ''
	descricao = ''
	fotos = []

	def __init__(self, sopa):
		self.__sopa = sopa
		self.bs = BeautifulSoup(self.__sopa, 'html.parser')

	def __pega_titulo__(self):
		self.titulo = self.bs.find('h1').string

	def __pega_preco__(self):
		self.preco = self.bs.find('span', class_='price-tag-fraction').string
		print(self.preco)

	def __fotos__(self):
		div = self.bs.find('div', class_='item-gallery__wrapper')
		imgs = div.findAll('img')

		for img in imgs:
			self.fotos.append(img['src'])

	def __descricao__(self):
		self.descricao = self.bs.find('div', class_='item-description__text')

		
Raspador().get()