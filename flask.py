"""Output response code, response time, page title to Prometheus metrics."""
import re
import requests

URL = 'http://localhost:5050'

response = requests.get(URL,timeout=10000)
result = re.search(r"<title>(.*)<\/title>", response.text)
print(f'response_code{{app="flask",method="get",title="{result.group(1)}"}} {response.status_code}')
print(f'response_latency{{app="flask",method="get"}} {response.elapsed.total_seconds()}')

response = requests.post(f'{URL}/update',timeout=10000)
result = re.search(r"<title>(.*)<\/title>", response.text)
print(f'response_code{{app="flask",method="update",title="{result.group(1)}"}}',
      f'{response.status_code}')
print(f'response_latency{{app="flask",method="update"}} {response.elapsed.total_seconds()}')

response = requests.post(f'{URL}/add',data={'todo_item': ''},timeout=10000)
result = re.search(r"<title>(.*)<\/title>", response.text)
print(f'response_code{{app="flask",method="add",title="{result.group(1)}"}} {response.status_code}')
print(f'response_latency{{app="flask",method="add"}} {response.elapsed.total_seconds()}')
