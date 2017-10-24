import requests
from bs4 import BeautifulSoup
import string
url = 'https://www.bayerpet.com.br/caes/lista-nomes/'



for c in string.ascii_uppercase:
    for p in (1, 2, 3):
        url2 =c+"/"+str(p)
        r = requests.get(url+url2)
        print (url+url2)
        bsObj = BeautifulSoup(r.text, "html.parser")
        dogs = bsObj.findAll("ul", {"class":"list listNames"})
        for cathoro in dogs:
            print (cathoro.getText())





'''            dogs = []
for c in string.ascii_uppercase:
  for p in (1, 2, 3):
    pg = c+'/'+str(p)
    page = requests.get(url + pg)
    print (url + pg)
    soup = BeautifulSoup(page.content, 'html.parser')
    lista = soup.find('ul', {'class':'list listNames'})
    lista_dogs = lista.findAll('li')
    for d in lista_dogs: dogs.append(d.string)
    
dogs.sort()
print (' '.join(dogs))
'''

      
      
