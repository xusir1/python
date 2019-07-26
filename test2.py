import urllib
import urllib2

values = {"unsername":"xulei","password":"1234"}
data = urllib.urlenconde
url = "https://wiki.synyi.com"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()