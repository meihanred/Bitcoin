__author__ = 'meihanred'
import json
from pprint import pprint
import urllib2

json_file='bitcoin_onion.json'
cube='1'

json_data=open(json_file)
data = json.load(json_data)
#pprint(data)
json_data.close()


hits = data['hits']['hits']
address = hits[40000]['fields']['bitcoin_addresses'][0]
addressinfo = json.load(urllib2.urlopen('http://btc.blockr.io/api/v1/address/info/'+address))
print addressinfo['data']['first_tx']['block_nb']