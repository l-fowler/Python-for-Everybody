"""
Exercise 1: Change either geojson.py or geoxml.py to print out the two-character country
code from the retrieved data. Add error checking so your program does not traceback if the
country code is not there. Once you have it working, search for “Atlantic Ocean” and make
sure it can handle locations that are not in any country.

You can download files from:
http://www.py4e.com/code3/geojson.py and www.py4e.com/code3/geoxml.py
"""

# Based on http://www.py4e.com/code3/geojson.py

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    print(js)
    # Counter variable for each item in address_components = -1 so start on [0]
    count = -1
    # New variable = js['results'][0]['address_components'][0]
    x = js['results'][0]['address_components']
    for item in x:
        count += 1
        # If/Else so if 'country', 'political' not found in [address_components][count] for loop continues
        if js['results'][0]['address_components'][count]['types'] == ['country', 'political']:
            # print short_name inside of address_components, inside of results
            print("Two-character country code: " + js['results'][0]['address_components'][count]['short_name'])
            break
        else:
            continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
