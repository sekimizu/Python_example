import urllib.request
import json

#serviceUrl = "http://maps.googleapis.com/maps/api/geocode/json?"
serviceUrl = "http://py4e-data.dr-chuck.net/json?"
api_key = 42

while True:
    #address = "South Federal University"
    #address = "Tallinn University"
    address = input('Enter location:')
    if len(address) < 1: break
    
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key

    url = serviceUrl + urllib.parse.urlencode(parms)
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("== Failure ==")
        print(data)
        continue

    #print(json.dumps(js, indent = 4))
    place_id = js["results"][0]["place_id"]
    print("Place id", place_id)
    """
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    print("lat", lat, "lng", lng)

    location = js["results"][0]["formatted_address"]
    print(location)
    """
    break