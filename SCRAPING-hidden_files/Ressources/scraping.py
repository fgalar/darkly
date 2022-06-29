import requests
from bs4 import BeautifulSoup
import sys

def scrapping_recursive(url):
  r = requests.get(url)
  s = BeautifulSoup(r.text, 'html.parser')
  if (s is not None):
    links = s.find_all("a")
    f = open("results.txt", "a+")
    for link in links:
      final_link = link['href']
      if (final_link == "README"):
        r = requests.get(url + final_link)
        if ' ' not in r.text and 'Demande' not in r.text:
          f.write(r.text)
          sys.exit('done')
      elif (final_link != "../"):
          scrapping_recursive(url + final_link)
    f.close()

scrapping_recursive("http://192.168.1.87/.hidden/")
