import requests
import json

url = 'http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/backendAmbiente/webresources/generic/getAllEstaciones'
#url_1 = 'http://ec2-54-202-254-90.us-west-2.compute.amazonaws.com:8080/backendAmbiente/webresources/generic/getAllSensores'
r = requests.get(url)
if r.status_code==200:
    data = r.json()
    for i in range(len(data)):
        a = data[i]
        elementos = a.items()
        for clave, valor in elementos:
            print clave,"= ", valor
else:
    print "error"

# data_string = json.dumps(data)
# decoded = json.loads(data_string)


## https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
