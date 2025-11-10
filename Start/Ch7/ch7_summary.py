import urllib.request
import json

# just try to open the url
web_url = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
# print("Result code: ", web_url.getcode())

# now read the page
data = web_url.read()
theJson = json.loads(data)  # this parses the json string into a python dictionary
print (theJson["text"])

