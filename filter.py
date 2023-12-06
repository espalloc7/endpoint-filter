import requests

# Read the endpoints from the text file
with open('endpoints.txt', 'r') as f:
    endpoints = f.read().splitlines()

alive = []
for endpoint in endpoints:
    try:
        response = requests.get(endpoint)
        # If the response does not contain '401', add it to the list
        if '401' not in response.text.lower():
            alive.append(endpoint)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with endpoint {endpoint}: {e}")

# Write the alive urls to a new text file
with open('alive.txt', 'w', encoding='utf8') as f:
    for url in alive:
        f.write(url + '\n')
