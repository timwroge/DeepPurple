import urllib.request,urllib.parse
import json as parseJson
query = input ( 'Query: ' )
urllib.request.urlretrieve
query = urllib.parse.urlencode ( { 'q' : query } )
response = str(urllib.request.urlopen ( 'http://www.faroo.com/api?q='+query+"&start=1&length=10&l=en&src=news&f=json").read())
print(response)
