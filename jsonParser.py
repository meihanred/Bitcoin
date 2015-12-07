__author__ = 'meihanred'
import json
from pprint import pprint
import urllib2

json_file='bitcoin_onion.json'
json_data=open(json_file)
data = json.load(json_data)
#pprint(data)
json_data.close()
f = open('addrlist', 'w+')
d = dict()
hits = data['hits']['hits']
count = 0
def WriteAddrToList():
    for x in range(0,50000):
        for each in hits[x]['fields']['bitcoin_addresses']:
            if d.get(each)!=1:
                d[each] =1
                f.write(each+'\n')
    print len(d)
WriteAddrToList()

#addressinfo = json.load(urllib2.urlopen('http://btc.blockr.io/api/v1/address/info/'+address))
#print addressinfo['data']['first_tx']['block_nb']