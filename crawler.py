#/usr/bin/python3

import re
import sys
import requests

# Get full url of site argument
URL = "https://" + sys.argv[1]

# Try get url response
try:
    site = requests.get(URL)
except:
    print(site)
    print("There is a problem reaching the URL provided")

# Assign site page
page = site.text
# Initiate site urls
relative_urls = ""

print("Urls found:\n")

# Scan for full urls
full_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', page)
print(str(full_urls))

# Scan for path segments and format in URL
path_segments = re.findall('href=\"(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+.php', page)
for x in path_segments:
    relative_urls += URL + "/"
    relative_urls += x[6:]
    relative_urls += "\n"

print(str(relative_urls))
