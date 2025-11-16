import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")
result = response.json()

# Get the latest conversion rate from USD to PHP
print(result['rates']['PHP'])
