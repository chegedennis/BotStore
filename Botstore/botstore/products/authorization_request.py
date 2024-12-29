"""
authorization_request.py

This module handles the authorization request to the Safaricom API to obtain an access token
using client credentials.
"""

import requests

# URL for the Safaricom OAuth token generation
url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
querystring = {"grant_type": "client_credentials"}
payload = ""

# Authorization header with Base64 encoded client credentials
headers = {
    "Authorization": "Basic SWZPREdqdkdYM0FjWkFTcTdSa1RWZ2FTSklNY001RGQ6WUp4ZVcxMTZaV0dGNFIzaA=="
}

# Make the GET request to the API
response = requests.request(
    "GET", url, data=payload, headers=headers, params=querystring
)

# Print the response status code and text
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    print("Response:", response.text)
else:
    print("Error:", response.text)
    print("Full Response:", response)
