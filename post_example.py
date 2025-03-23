import requests

# Define root
rt = 'https://hc-first-api.onrender.com'

# Define end point
u_creature = f"{rt}/creature"

# Define a payload
pl = {'HC': 'human'}

# Make a POST call
response = requests.post(url = u_creature, json = pl)

# Check response
if response.status_code == 201:
    json_response = response.json()
    print(json_response)
else:
    print(response.status_code)
    print(response.text)


