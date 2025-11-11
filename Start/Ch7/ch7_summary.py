import urllib.request

# ================== open an url ==================
# just try to open the url
web_url = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
# print("Result code: ", web_url.getcode())

# ================== read some json ==================
import json
# now read the page
data = web_url.read()
theJson = json.loads(data)  # this parses the json string into a python dictionary
print (theJson["text"])

# ================== read some xml ==================
import xml.dom.minidom as minidom
theXml = minidom.parse("samplexml.xml") # this file is at the root of the repo
print(theXml.nodeName)
print(theXml.firstChild.tagName)

new_skill = theXml.createElement("skill")
new_skill.setAttribute("name", "just added C++ as skill")
theXml.firstChild.appendChild(new_skill)

skills = theXml.getElementsByTagName("skill")
for skill in skills:
    print(skill.getAttribute("name"))