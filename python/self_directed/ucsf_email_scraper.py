import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


data = pd.read_csv('ucsf_residents.csv', index_col = 0)

which_500 = int(input("Which 500 do you want to do [1-4]: "))
to_save = 'ucsf_residents_with_email_{}.csv'.format(which_500)
#to_save = #input('CSV file to save to: ')

data['email'] = ''
data['uncertain_email'] = False

num_people = data.shape[0]

start = 500 * (which_500 - 1)
end = 500 * which_500
if end > num_people:
	end = num_people


counter = 0

def extract_email(row):
	global counter, num_people
	if counter >= start and counter <= end:
		try:
			name = row['name']
			print("{}/{}: {}".format(row.name,num_people,row['name']))

			query = 'https://directory.ucsf.edu/people/search/name/{}'.format(name)
			
			response = requests.get(query)
			soup = BeautifulSoup(response.content,"html.parser")

			links = [each for each in soup.findAll('a') if 'mailto' in each['href']]

			row['email'] = links[0]['href'].split('mailto:')[1]
			row['uncertain_email'] = len(links) > 1
		except Exception as e:
			row['uncertain_email'] = True
			print("Error getting email\n")
	counter += 1
	return row

data = data.apply(extract_email, axis=1)


data.to_csv(to_save)