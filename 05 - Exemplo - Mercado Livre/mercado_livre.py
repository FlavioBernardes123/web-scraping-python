# > EXEMPLO
# - Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usu�rio

import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    print(produto.prettify())
    print('T��tulo do produto:', titulo.text)
    print('Link do produto:', link['href'])

    if (centavos):
        print('Pre�o do produto: R$', real.text + ',' + centavos.text)
    else:
        print('Pre�o do produto: R$', real.text)
    
    print('\n\n')
    break
