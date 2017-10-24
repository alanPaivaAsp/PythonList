import requests
from bs4 import BeautifulSoup
url = 'https://sismpconsultapublica.mpsp.mp.br/ConsultarDistribuicao/ObterFiltrosPorMembro'
r=requests.get(url)
filhosdaputa = BeautifulSoup(r.content, "html.parser")
fdp = filhosdaputa.findAll("select", {"id":"Membro"})
for fdp2 in fdp:
    print(fdp2.getText())
