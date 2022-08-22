import requests, sys, bs4,csv

baseUrl= 'https://google.com/search?q='

def searchUrlF(text):
    baseU = text.replace(' ', '+')

    return baseUrl + baseU

# stablish search
searchUrl = searchUrlF('pineapple')



print(len(sys.argv))
if(len(sys.argv) == 2):
    pp = sys.argv[1]
    print(pp.split(','))
    exclude = pp.split(',')

    # x = range(len(ex))
    for excl in exclude:
        searchUrl = searchUrl + "+-site%3A"+excl

print(searchUrl)



def fetchPage(linkFetched):
    res = requests.get(linkFetched)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    return soup

soup = fetchPage(searchUrl)

linkE = soup.select('div#main > div > div > div > a')

for i in range(len(linkE)):
    print(linkE[i].get('href'))

f = open("act2t2.csv", "a", newline="")
writer = csv.writer(f)


for i in range(len(linkE)):
    writer.writerow((linkE[i].text+',', linkE[i].get('href')))

f.close()