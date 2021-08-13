import requests, re
from pprint import pprint

#<a href="" class="feed-post-link gui-color-primary gui-color-hover" elementtiming="text-csr">Cidade de SP fará 'xepa' para antecipar 2ª dose da vacina; veja regras</a>

def getTitulos(url):
    req = requests.get(url)
    #tags = re.findall(r'(<p class="descricao">)(.+?)(<\/p>)', str(req.content))
    #tags = re.findall(r'(elementtiming="text-ssr">)(.+?)(<\/a>)', str(req.content))
    
    tags = re.findall(r'(<a href=".+?" class="feed-post-link gui-color-primary gui-color-hover" elementtiming="text-ssr">)(.+?)(<\/a>)', str(req.content))
    
    titleList = []

    for tag in tags:
        um,dois,tres = tag
        titleList.append(dois)

    return titleList
