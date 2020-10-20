import requests

for i in range(10,60):
    req = requests.get("http://rekru.kn-bit-cyber.ninja/division?id="+str(i)+"")
    print (req.status_code)
    print (req.text)
