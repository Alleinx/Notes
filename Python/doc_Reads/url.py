import urllib.request
import urllib.parse

# Receive data:
req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    # print(the_page)

# Send data with POST()
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {
    'name': 'Michael Foord',
    'locaation': 'Northampton',
    'language': 'Python'
}

# -----------------------------------
# Encode Data into the standard required by HTML
data = urllib.parse.urlencode(values)

data = data.encode('ascii') # Data should be bytes
req = urllib.request.Request(url, data)

# with urllib.request.urlopen(req) as response:
    # the_page = response.read()
    # print(the_page)

# -----------------------------------
# Could also pass data in HTTP GET request by encoding data in the URL itself.
url_values = urllib.parse.urlencode(values)
print(url_values)

url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values
# data = urllib.request.urlopen(full_url)

# -----------------------------------
# Set headers
url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)

# with urllib.request.urlopen(req) as response:
#    the_page = response.read()

# -----------------------------------
# URL Exception
req = urllib.request.Request('http://www.pretend_server.org')
try:
    urllib.request.urlopen(req)

except urllib.error.URLError as e:
    print(e.reason)