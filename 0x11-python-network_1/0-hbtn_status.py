import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
  body = response.read()
  print(type(body))
  print(body)

