import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

m = MultipartEncoder({'roomId': 'Y2lz....',
                      'text': 'example message'})

r = requests.post('https://webexapis.com/v1/messages', data=m,
                  headers={'Authorization': 'Bearer TOKEN',
                  'Content-Type': m.content_type})

print(r.text)
