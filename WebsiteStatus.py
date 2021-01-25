 # Checks status of a website and reports if down
 #
 # Created By: Charles Cromer
 # Created On: January 07, 2021
 # Last Edit: January 20, 2021

import ezgmail, urllib.request, urllib.error, os, time, datetime, requests, sys

ezgmail.init()

URL = 'ENTER WEBSITE TO HAVE UPTIME TRACKED'
PHONE = 'ENTER EMAIL ADDRESS OF CELL PHONE'
EMAIL = 'ENTER EMAIL ADDRESS'

# Sends a header that simulates this request is coming from a personal web browser instead of a python program
# Many times a request will be denied if it appears it is coming from a python program
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

CREDPATH = r'ENTER DIRECTORY PATH TO THIS APPLICATION, MUST HAVE GMAIL CREDENTIAL FILES'

os.chdir(r'{}'.format(CREDPATH))

while True:

    now = datetime.datetime.now()
    nowF = now.strftime('%Y-%m-%d %H:%M:%S')

    try:
        # Gets header response from desired website
        response = requests.get(URL, headers = headers)

        # If website is working (200) simply prints a working status
        # If there is any http error such as status 400, it sends this info
        # to the designated phone and email
        if response.status_code != 200:
            statusUpdate = nowF + " Website Alert!: " + str(response.status_code)

            ezgmail.send(PHONE, 'Website Alert!', statusUpdate)
            ezgmail.send(EMAIL, 'Website Alert!', statusUpdate)

            print(statusUpdate)
        else:
            print(nowF, "Working: ", response.status_code)

    # Catches any/all other program errors, prints them on the display and continues running the program
    except:
        print(now)
        print('Unexpected Error: ', sys.exc_info())

    # Pauses status requests for one minute
    time.sleep(60)
