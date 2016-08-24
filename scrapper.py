import urllib
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox() #theoretically we should be able to use PhantomJS but for some reason it isnt able to detect element by id
driver.set_window_size(550, 550)

driver.get('https://hartfordhospital.org/find-a-doctor/search-results?AcceptingNewPatients=True')
html = requests.get("https://hartfordhospital.org/find-a-doctor/search-results?AcceptingNewPatients=True")

doc_url = ''
doc_name = ''
doc_tel = ''
doc_spec = ''
doc_add = ''
doc_add_url = ''

soup = BeautifulSoup(html.content, "html.parser")

for details in soup.findAll("tr"):
	for name_tel in details.findAll("a", href=True):
		if name_tel.get('href').startswith('/find-a-doctor/physician-detail?id=') and name_tel.text:
			global doc_url
			global doc_name
			doc_url = 'https://hartfordhospital.org' + name_tel.get('href')
			doc_name = name_tel.text
		if name_tel['href'].startswith('tel://'):
			global doc_tel
			doc_tel = name_tel.text
	for specialities in details.findAll("li", id=True):
		if specialities.get('id').endswith('liSpecialty'):
			global doc_spec
			doc_spec = specialities.text.strip()
	for locations in details.findAll("li", id=True):
		if locations.get('id').endswith('liLocation'):
			global doc_add
			doc_add = locations.text.strip()[:-16]
	for address in details.findAll("a", href=True):
		if address.get('href').startswith('https://maps.google.com/?'):
			global doc_add_url
			doc_add_url = address.get('href') 
	payload = {'Doctors': doc_name, 'Directory Url': doc_url, 'Telephone #': doc_tel, 'Specialities': doc_spec, 'Locations': doc_add + doc_add_url}
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	requests.post('https://sheetsu.com/apis/v1.0/9c74cacddfe8', data=json.dumps(payload), headers=headers)

driver.find_element_by_id('ctl11_ppDataPagerTop_lbNext').click()
