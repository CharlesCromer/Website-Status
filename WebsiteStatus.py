 # Checks status of a website and reports if down
 #
 # Created By: Charles Cromer
 # Created On: January 07, 2021
 # Last Edit: January 07, 2021

import ezgmail, urllib.request, os, time

ezgmail.init()

URL = ''
PHONE = ''

response = urllib.request.urlopen(URL)
status_code = response.getcode()
