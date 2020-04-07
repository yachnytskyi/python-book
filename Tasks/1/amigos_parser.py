from bs4 import BeautifulSoup
import requests

def conjugation(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    content = response.text
    soup = BeautifulSoup(content, "lxml")
    objects = dict()
    divs = soup.findAll('div', {'class': 'fldiv'})
    for div in divs:
        header = div.find('h3')
        tables = div.findAll('table', {'class': 'blok'})
        objects[header.text.strip()] = {}
        for table in tables:
            tds = table.findAll('td')
            th = table.find('th')
            values = [td.text for td in tds]
            words = values[::2]
            values = values[1::2]
            result = list(zip(words, values))
            result = dict((x.strip(), y.strip()) for x, y in result)
            objects[header.text][th.text.strip()] = result
    return objects

url = 'https://entre-amigos.ru/components-loco/conjugator/getuser.php?q=acabar'
data = conjugation(url)
print(data)
