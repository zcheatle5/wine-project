import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'temp':67.9, 'grapes_in_first_year':200, 'grapes_in_third_month':400})

print(r.json())