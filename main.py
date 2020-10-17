from bs4 import BeautifulSoup
import requests

medicoverSite = requests.get('https://mol.medicover.pl')
print(medicoverSite.text)
soup = BeautifulSoup(medicoverSite, 'html.parser')
print(soup.prettify())