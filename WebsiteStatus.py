 # Checks status of a website and reports if down
 #
 # Created By: Charles Cromer
 # Created On: January 07, 2021
 # Last Edit: January 08, 2021

import ezgmail, urllib.request, urllib.error, os, time

ezgmail.init()

URL = ''
PHONE = ''
EMAIL = ''

while True:

    try:
        response = urllib.request.urlopen(URL)

    except urllib.error.HTTPError as e:
        print('HTTPError: {}'.format(e.code))
        ezgmail.send(PHONE, 'Website Alert!', 'HTTPError: {}'.format(e.code) )
        ezgmail.send(EMAIL, 'Website Alert!', 'HTTPError: {}'.format(e.code) )

    except urllib.error.HTTPError as e:
        print('HTTPError: {}'.format(e.reason))
        ezgmail.send(PHONE, 'Website Alert!', 'HTTPError: {}'.format(e.reason) )
        ezgmail.send(EMAIL, 'Website Alert!', 'HTTPError: {}'.format(e.reason) )

    finally:
        time.sleep(360)
