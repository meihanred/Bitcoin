__author__ = 'meihanred'
import json
from pprint import pprint
import urllib2
import blocktrail
json_file='bitcoin_onion.json'
json_data=open(json_file)
data = json.load(json_data)
#pprint(data)
json_data.close()
d = dict()
hits = data['hits']['hits']
count = 0

def WriteAddrToList():
    addresses = []
    f = open('addrlist','w+')
    for x in range(0,50000):
        for each in hits[x]['fields']['bitcoin_addresses']:
            if d.get(each)!=1:
                d[each] =1
                addresses.append(each);
                f.write(each+'\n')
#WriteAddrToList()


def findTxs():
    with open('addrlist') as f:
        lines = f.readlines(1)
    nb_over_200 = 0
    total=0
    largest_txs_nb = 0
    for line in lines:

        addressinfo = json.load(urllib2.urlopen('http://btc.blockr.io/api/v1/address/info/'+line))
        nb_txs =  addressinfo['data']['nb_txs']
        total += nb_txs
        if nb_txs >200:
            nb_over_200 += 1
        if nb_txs > largest_txs_nb:
            largest_txs_nb = nb_txs
        print line +"   " + str(nb_txs)
    avg_nb_txs = total/len(lines)
    print "Average number of transactions for all addresses is " + str(avg_nb_txs)
    print "Number of addr with more than 200 transactions is " + str(nb_over_200)
    print "Largest number of transactions for an address is " + str(largest_txs_nb)
#findTxs()


# addressinfo = json.load(urllib2.urlopen('https://bitcoin.toshi.io/api/v0/addresses/1Nb5hT7DqwSHt9uUno68Y4YwDGRnTd36Z8/transactions'))
# print addressinfo['transactions']
# print len(addressinfo['transactions'])

print client.address('1NcXPMRaanz43b1kokpPuYDdk6GGDvxT2T')