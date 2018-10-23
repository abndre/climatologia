# - coding: utf-8 --
import bs4
from bs4 import BeautifulSoup
import requests

#outro arquivo
from output import diciostat_abrev, diciostate_cities, listastat

#global list with value
#like: [{'cidade': 'Acrelândia', 'estado': 'AC'}, {'Janeiro': {'min': '23°', 'max': '29°', 'pres': '298'}, 'Fevereiro': {'min': '23°', 'max': '28°', 'pres': '286'}, 'Março': {'min': '23°', 'max': '28°', 'pres': '290'}, 'Abril': {'min': '22°', 'max': '29°', 'pres': '210'}, 'Maio': {'min': '21°', 'max': '29°', 'pres': '107'}, 'Junho': {'min': '20°', 'max': '31°', 'pres': '38'}, 'Julho': {'min': '20°', 'max': '32°', 'pres': '24'}, 'Agosto': {'min': '22°', 'max': '35°', 'pres': '42'}, 'Setembro': {'min': '24°', 'max': '35°', 'pres': '97'}, 'Outubro': {'min': '23°', 'max': '33°', 'pres': '169'}, 'Novembro': {'min': '23°', 'max': '31°', 'pres': '233'}, 'Dezembro': {'min': '23°', 'max': '29°', 'pres': '252'}}]

lista = []

#remove unicodes
from unicodedata import normalize
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

#get values from link
def gettemperatura(link):
    print(link)
    #link = 'https://www.climatempo.com.br/climatologia/2/santos-sp'
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')

    dicio={}
    for i in soup.find('tbody'):
        try:
            key = i.find('td',{'class':"text-center normal font14 txt-blue"}).string
            dicio[key]=[]
            for j in i.find_all('td',{'class':"text-center normal font14 txt-black"}):
                value = j.string
                dicio[key].append(value)
        except:
            #TODO tratar erro
            #Possivel mais erros
            pass

    #criando chave valor
    dicio2 = {}
    for key, value in dicio.items():
        dicio2[key]={'min':value[0],'max':value[1], 'pres':value[2]}

    l = soup.title.string.split(' - ')
    del l[0]
    lista.append([{'cidade':l[0],'estado':l[1]}, dicio2])

for state in listastat:
    listacities_dicio = diciostate_cities[state]
    for key, value in listacities_dicio.items():
        id  = (value)
        city=(remover_acentos(key).lower())
        city=city.replace(' ','')
        city=city.replace("'",'')
        statelower=(diciostat_abrev[state].lower())
        #e.g: 'https://www.climatempo.com.br/climatologia/2/santos-sp'
        link = 'https://www.climatempo.com.br/climatologia/{}/{}-{}'.format(id,city,statelower)
        gettemperatura(link)

    #Limit for test
    if len(lista)>=100:
        break
