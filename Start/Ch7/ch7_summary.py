import urllib.request

# just try to open the url
web_url = urllib.request.urlopen("http://example.com")
print("Result code: ", web_url.getcode())

# now read the page
data = web_url.read()
print (data)

