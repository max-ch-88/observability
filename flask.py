# Output response code, response time, page title to Prometheus metrics
import requests
import re

url = 'http://localhost:5050'

response = requests.get(url)
result = re.search(r"<title>(.*)<\/title>", response.text)
print('response_code{{app="flask",method="get",title="{0}"}} {1}'.format(result.group(1), response.status_code))
print('response_latency{{app="flask",method="get"}} {0}'.format(response.elapsed.total_seconds()))

response = requests.post(f'{url}/update')
result = re.search(r"<title>(.*)<\/title>", response.text)
print('response_code{{app="flask",method="update",title="{0}"}} {1}'.format(result.group(1), response.status_code))
print('response_latency{{app="flask",method="update"}} {0}'.format(response.elapsed.total_seconds()))

response = requests.post(f'{url}/add',data={'todo_item': ''})
result = re.search(r"<title>(.*)<\/title>", response.text)
print('response_code{{app="flask",method="add",title="{0}"}} {1}'.format(result.group(1), response.status_code))
print('response_latency{{app="flask",method="add"}} {0}'.format(response.elapsed.total_seconds()))
