from requests import post
import json
payload = {'product_id': 'B014F6U5N6', 'website_name': 'amazon.in', 'url': 'xyz'}
r = post("http://localhost:5000", json.dumps(payload), headers={'Content-Type': 'application/json'})
print r.text
