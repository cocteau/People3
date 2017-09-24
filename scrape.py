from urllib import urlopen
url = "http://brown.columbia.edu/about"

from bs4 import BeautifulSoup

bs = BeautifulSoup(urlopen(url).read())

for d in bs.find_all("div"):

   if "style" in d.attrs: 
      if d["style"][:11] == "background:":
         print d["style"][11:]