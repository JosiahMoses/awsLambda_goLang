import urllib.request

ipAddress = input("Enter IP: ")

urlToRead = "http://ipwhois.app/json/" + ipAddress
try:
   with urllib.request.urlopen(urlToRead) as f:
      print(f.read().decode('utf-8'))
except urllib.error.URLError as e:
   print(e.reason)