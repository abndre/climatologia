# - coding: utf-8 --
import bs4
from bs4 import BeautifulSoup
import requests

#outro arquivo
from output import diciostat_abrev, diciostate_cities, listastat

lista = []

from unicodedata import normalize
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


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
            pass

    dicio2 = {}
    for key, value in dicio.items():
        dicio2[key]={'min':value[0],'max':value[1], 'pres':value[2]}

    l = soup.title.string.split(' - ')
    del l[0]
    lista.append([{'cidade':l[0],'estado':l[1]}, dicio2])

for state in listastat:
    listacities_dicio = diciostate_cities[state]
    #print(listacities_dicio)
    for key, value in listacities_dicio.items():
        id  = (value)
        city=(remover_acentos(key).lower())
        city=city.replace(' ','')
        city=city.replace("'",'')
        #https://www.climatempo.com.br/climatologia/5727/olhod'aguadocasado-al
        #print(diciostat_abrev(state).lower())
        statelower=(diciostat_abrev[state].lower())
        #print(key,value)
        #e.g: 'https://www.climatempo.com.br/climatologia/2/santos-sp'
        link = 'https://www.climatempo.com.br/climatologia/{}/{}-{}'.format(id,city,statelower)
        gettemperatura(link)

    #Limit for test
    if len(lista)>=100:
        break
