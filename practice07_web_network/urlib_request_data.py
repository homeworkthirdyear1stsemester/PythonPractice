import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}
url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)

with urllib.request.urlopen(url) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(r)

payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request('http://httpbin.org/post', method='POST')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

req = urllib.request.Request('http://httpbin.org/put', method='PUT')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

req = urllib.request.Request('http://httpbin.org/delete', method='DELETE')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))
