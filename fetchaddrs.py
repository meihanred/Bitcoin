__author__ = 'meihanred'
import json
from pprint import pprint
import urllib2
import blocktrail
import blocktrailAPI
import urlparse
from collections import defaultdict
from multiprocessing import Process
from multiprocessing import Pool
import os
import time
def readJson():
    json_file='bitcoin_onion.json'
    json_data=open(json_file)
    data = json.load(json_data)
    #pprint(data)
    json_data.close()
    hits = data['hits']['hits']
    return hits
def WriteAddrToFile():
    d = dict()
    addresses = []
    f = open('addrlist','w+')
    hits = readJson()
    for x in range(0,50000):
        for each in hits[x]['fields']['bitcoin_addresses']:
            if d.get(each)!=1:
                d[each] =1
                addresses.append(each);
                f.write(each+'\n')
#WriteAddrToFile()

def getURLs():
    URLs = []
    d = defaultdict(list)
    hits = readJson()
    nb_no_url_attr = 0
    for x in range(0,50000):
      addressgroup = hits[x]['fields']['bitcoin_addresses']
      try:
        for each in hits[x]['fields']['url']:

            domain =  urlparse.urljoin(each, '/')

            if 'https' in domain.lower():
                index = domain.lower().index('https')
                domain = domain[index+8:]

            elif 'http' in domain.lower():
                index = domain.lower().index('http')
                domain = domain[index+7:]

            if 'www' in domain:
                index = domain.index('www')
                domain = domain[index+4:]

            for eachaddr in addressgroup:
                # if eachaddr not in d.get(domain):
                if eachaddr not in list(d[domain]):
                    d[domain].append(eachaddr)
      except KeyError:
          nb_no_url_attr += 1
          continue
    print  "There are " + str(len(d)) + " keys, and accroding numbers of values are: "
    f = open('url_addr','w+')
    sorted(d, key=d.get, reverse=True)

    for each in sorted(d, key=lambda k: len(d[k]), reverse=True):
        print (each + "--------" + str(len(d.get(each))) )
        f.write(each + "--------" + str(len(d.get(each))) + '\n' )


getURLs()

# addressinfo = json.load(urllib2.urlopen('https://bitcoin.toshi.io/api/v0/addresses/1Nb5hT7DqwSHt9uUno68Y4YwDGRnTd36Z8/transactions'))
# print addressinfo['transactions']
# print len(addressinfo['transactions'])
