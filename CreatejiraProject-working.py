# importing the requests library
import requests
import json

# defining the api-endpoint
API_URL = "https://dot-jira-d.lilly.com/rest/project-templates/1.0/createshared/10700"

headers = {
    'Content-Type': 'application/json',
}

data1 = {
    'key': 'NEWKEY55',
    'lead': 'c261779',
    'name': 'NEWPROJNAME55'
}

response = requests.post(url=API_URL, headers=headers, auth=('c261779', 'Sailu1719'), data=json.dumps(data1))
