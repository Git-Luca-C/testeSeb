from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import openpyxl as op

#get no url informado para o webscrapping
req = requests.get("https://gruposeb.gupy.io/")
site = bs(req.content, 'html.parser')
dados = site.findAll('a', attrs={'data-testid': 'job-list__listitem-href'})

#criando um array vazio com a estrutura adequada para receber os dados
arr_vagas = np.empty((len(dados),), dtype=object)

#percorrendo os elementos encontrados
for i, vaga in enumerate(dados):
    #pegar as 'divs' dentro de cada <li>
    divs = vaga.find('div')

    #pegar o texto de cada 'div' e adicionar na lista de vagas
    arr_vagas[i] = [div.get_text(strip=True) for div in divs]

#print no console os dados capturados
for vaga in arr_vagas:
    print(vaga)

#formatar um excel com o retorno do webscrapping
workbook = op.Workbook()
sheet = workbook.active

head = ["Cargo", "Localidade", "Efetividade"]
sheet.append(head)

for vagas in arr_vagas:
    sheet.append(vagas)

workbook.save('vagas_seb.xlsx')