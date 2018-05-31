import requests
from lxml import html
from lxml import etree


#Get the CSRF_TOKEN from sign-in page
login_url = "https://nomadhealth.com/sign-in"

session_requests = requests.session()

result = session_requests.get(login_url)

tree = html.fromstring(result.text)

authenticity_token = list(set(tree.xpath("//input[@name='csrf_token']/@value")))[0]

#print(authenticity_token)


#my login info
login_info = {
	"email": "justin.d.krogue@gmail.com",
	"password": "password1234",
	"csrf_token": authenticity_token
}

#Login
result = session_requests.post(login_url, data = login_info, headers = dict(referer=login_url))

#Scrape results
url = "https://nomadhealth.com/search?jobTypes=locums"
result = session_requests.get(url, headers = dict(referer=url))

tree = html.fromstring(result.content)

#print(tree.tostring())

body = tree.xpath('//body')
result = ""
for each in body:
	result += "\n" + str(etree.tostring(each, pretty_print = True))

with open("output.html","w") as file:
	file.write(result)

opp_names = tree.xpath('//div[@class="Select-placeholder"]')

#print(opp_names)

print(opp_names)