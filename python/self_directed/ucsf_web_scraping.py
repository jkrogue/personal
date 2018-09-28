import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

#query = input("Enter the url of the first search page result: ")
query = 'https://profiles.ucsf.edu/search/default.aspx?searchtype=people&searchfor=&exactphrase=false&perpage=100&offset=0&page=1&totalpages=17&searchrequest=A81BSfTwU3GNm4liSODkW6vB3EBYO6gz+a5TY1bFhuz1tc7ngL4Orww3064KoquG+9VriFtrDjogfSknlN6Jz7ictMT0qk3g10zM0TMIEPsEyvmx6bLpcnNFGJ4exv4/fFAesBf4NHrkI4nVpsBeSKg1prKuDu5Ad3xZR2IG1VXzQt2Kl5Hs5a708T2/vlG+0DSye5g9KBjG4Q1kuBhnZNV3TLVPhoChvEqCnKALU7a7awqf6lAuskQW4rD5G/OC/lXclIHC7LtUeKfMKIzva4dDNw2yad/+Ztpp+7k5ZCyw78HL/ylb8xtpoTCrpOCblNkbtcHNwmWVhmKSEotaCdKtPoDL1Ce/aO+YXYcU6KD7Dlz0pELaBELBAK3AHzviWhAZoEO2zSaCANZthTN7c44rLpKsCtzJB1J8saJBnpOTxxslByFeuLnuGABya0glzpReNVD92uMxK9X3nHMQumkjPT995CvslFBfA02sgeXmwZLkx9b5lEnfV/zWSUU4+fQwO2wYwJHX2RTAc9SWtVCwsLPQBbJ/2L5GyfId6jCILA5IJH6KvQWbPY/XBgX+Hk2w/aIiEEiSPL2qnX6ciUDcfof+wDlLjkgKuchLbbGCANZthTN7c1mg7RaRHDbO9bXO54C+Dq8MN9OuCqKrhv/QtV0VC1l/tncZFI6GsA7IpJFAbogWvUSniam10xyZzMtUtPFkvKSqnPEO7gfPsl3taATzidUkHiA5/1D/YFLtyfQuU1EJK8mZk0QlNEbahfDRk6WWackXzoprXw9N3K6aZoyBVRbYhRlIQH6ysdDG1wiODD4wmDvusvk5GeZpRyV230E16h5+YNtqZyNkK3ZLK/QkvdTaWPPp2cGxYrrZiGAOzXr4waSMi7j4WrJToPTFRtD/QI8=&sortby=&sortdirection=&showcolumns=10'

m = re.search(r'&totalpages=([0-9]+)',query)
if m:
	total_pages = int(m.group(1))
else:
	exit("invalid url")
print(total_pages)
curr_page = 1

filename = input("Where to save csv output: ")

names = []
departments = []
profiles = []
types = []

NAME_INDEX = 0
DPT_INDEX = 1
TYPE_INDEX = 2

TOTAL_CELLS = 3

while True:
	print("Page: {}/{}".format(curr_page,total_pages))

	response = requests.get(query)
	soup = BeautifulSoup(response.content,"html.parser")

	result_table = soup.findAll(id='tblSearchResults')[0]
	rows = result_table.findAll('tr')
	for each in rows:
		cells = each.findAll('td')

		if len(cells) < TOTAL_CELLS:
			continue


		try:
			name_cell = cells[NAME_INDEX]
			names.append(name_cell.contents[0].split(',')[0])
			profile_link = 'https{}'.format(name_cell['onclick'].split('https')[1])
			profiles.append(profile_link)
			departments.append(cells[DPT_INDEX].contents[0])
			types.append(cells[TYPE_INDEX].contents[0])
		except Exception as e:
			print(cells[NAME_INDEX])

	'''
	links = soup.findAll("a", attrs={ "class" : "listTableLink"})
	for each in links:
		content = each.contents[0]
		if 'why' not in content.lower():
			names.append(content.split(',')[0])
			profiles.append(each['href'])
	#print(names)
	'''

	curr_page += 1
	if curr_page > total_pages:
		#print(query)
		break
	else:
		query = re.sub(r'&page=([0-9]+)', '&page={}'.format(curr_page), query)


data = pd.DataFrame({'name': names, 'profile': profiles, 'department': departments, 'personnel_type': types})
data.to_csv(filename)
