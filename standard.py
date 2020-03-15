from bs4 import BeautifulSoup
import requests

CONST_QUERY_URL = 'https://www.monster.com/jobs/q-remote-jobs?jobid='
response = requests.get('https://www.monster.com/jobs/q-remote-jobs')
# print(response.text)
responseTxt = response.text
soup = BeautifulSoup(responseTxt, 'lxml')

for jobId in soup.findAll(attrs={"data-jobid" : True}):
     jobid = jobId['data-jobid']
     print(CONST_QUERY_URL + jobid)


# for x in match:
#      print(x)

# print(match)
# with open('indeed.html', 'w') as f:
#      f.write(str(match))  

