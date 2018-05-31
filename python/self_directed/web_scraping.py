import requests
from lxml import html



#my login info
login_info = {
	"email": "justin.d.krogue@gmail.com",
	"password": "password1234",
	"csrf_token": "1523907100##dcfd088156ddbd1867c7a9395d77f19c5216ae19"
}

login_url = "https://nomadhealth.com/sign-in"

session_requests = requests.session()

result = session_requests.get(login_url)

tree = html.fromstring(result.text)

authenticity_token = list(set(tree.xpath("//input[@name='csrf_token']/@value")))[0]

