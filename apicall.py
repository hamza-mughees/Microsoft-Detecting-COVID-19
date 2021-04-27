# Ensure your pyOpenSSL pip package is up to date


# Example posting a local image file:

import requests
r = requests.post(
    "https://api.deepai.org/api/torch-srgan", # needs changing
    files={
        'image': open('J:/Users/Jason/Pictures/Screenshots/Screenshot (79) - Copy.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}# needs changing
    print(r)
print(r.json())
