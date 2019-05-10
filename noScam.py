import os, json, string, requests, sys, time, csv
from random import randint


#chars = string.ascii_letters + string.digits + '!@#$%&^*/\\()[]'
#random.seed = (os.urandom(1024))

url = "https://staemcomrnnunutu.com/login/?goto=%2Ftradeoffer%2Fnew%2F%3Fpartner%3D866992754%26token%3DJ1hJ87SV"

i = 0

emails = ['gmail.com','web.de','yahoo.com','gmx.com','ok.de','mail.com','posteo.de','googlemail.com','hotmail.com','outlook.com']

with open('fakes.csv', 'rb') as f:
    reader = csv.reader(f)
    pseudodata = list(reader)

# remove headers
pseudodata.remove(['\xef\xbb\xbfEmailAddress', 'Username', 'Password']) 

#TODO add email header with row 12

for items in pseudodata:
    i += 1
    email = items[0]
    username = items[1]
    password = items[2]

    #username = randint(1111111111, 9999999999)
    #password = randint(1111111111, 9999999999)

    #name_extra = ''.join(random.choice(string.digits))
    #password = ''.join(random.choice(chars) for i in range(8))

    print str(i)+":"
    print 'sending %s,%s' % (username,password)

    #time.sleep(randint(1, 5));

    r = requests.post(url, allow_redirects=False, data={
        'doAuth':'1',
        'username': username,
        'text': password
    })
    if r.status_code == 200:
        print 'Yeah, he got ripped!'
    else:
        print r.status_code