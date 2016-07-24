import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# driver = webdriver.Firefox()

html = requests.get("https://hartfordhospital.org/find-a-doctor/search-results?AcceptingNewPatients=True")

soup = BeautifulSoup(html.content, "html.parser")

for details in soup.findAll("tr"):
	for name_tel in details.findAll("a", href=True):
		if name_tel.get('href').startswith('/find-a-doctor/physician-detail?id=') and name_tel.text:
			print 'https://hartfordhospital.org' + name_tel.get('href')
			print name_tel.text
		if name_tel['href'].startswith('tel://'):
			print name_tel.text
	for specialities in details.findAll("li", id=True):
		if specialities.get('id').endswith('liSpecialty'):
			print specialities.text.strip()
	for locations in details.findAll("li", id=True):
		if locations.get('id').endswith('liLocation'):
			print locations.text.strip()[:-16]
	for address in details.findAll("a", href=True):
		if address.get('href').startswith('https://maps.google.com/?'):
			print address.get('href') 

	print "\n"