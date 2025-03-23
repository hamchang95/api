import requests

# Define root
rt = 'https://hc-first-api.onrender.com'

# Define end point
u_creature = f"{rt}/creature"

# Make a GET call
response = requests.get(f"{u_creature}/Dunah")

# Check response
if response.status_code == 200:
    json_response = response.json()

    print(json_response)