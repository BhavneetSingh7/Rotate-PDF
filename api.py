import requests

url = "http://127.0.0.1:5000/"
file = 'tmp/BhavneetSingh-Resume2.pdf'
page_angles = '1:180'
payload={'page-angles': page_angles}
files=[
  ('pdf-file',('BhavneetSingh-Resume2.pdf',open(file,'rb'),'application/pdf'))
]

response = requests.request("POST", url, data=payload, files=files)

# print(response.text)
# print(response.content)
with open('tmp/output.pdf',mode='wb') as f:
    f.write(response.content)