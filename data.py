import urllib.parse
import urllib.request
import ssl

url1 = "https://catalog.unc.edu/undergraduate/programs-study/"


ssl._create_default_https_context = ssl._create_unverified_context

# Urlencode the URL
url1 = urllib.parse.quote_plus(url1)

# Create the query URL.
query1 = "https://api.scraperbox.com/scrape"
query1 += "?token=%s" % "848EE571F23C6D45A602D8AA75E6D01F"
query1 += "&url=%s" % url1

# Call the API.
request1 = urllib.request.Request(query1)
raw_response1 = urllib.request.urlopen(request1).read()
html1 = raw_response1.decode("utf-8")

html1 = html1[6942:30180]


for i in range(len(html1)):
    if html1[i:i+6] == "href":
        x: int = 0
        while html1[i+x] != ">":
            x += 1
        print(x)


        # html1[i+6:]