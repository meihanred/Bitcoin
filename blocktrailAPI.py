import blocktrail
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()



def readAddrtoArray():
    with open('addrlist') as f:
        lines = f.readlines(1)
        addresses = []
        for line in lines:
            line = line[:len(line)-1]
            addresses.append(line)
            if len(line) ==0:
                continue
    return addresses

def getTXS(address):
    client = blocktrail.APIClient("a59fcf92aabaa20cfb74c221b66a1202ab44565c", "c81e71b8784f840807efd73b3cb53d9ca0a04bcd")
    txs = client.address_transactions(address)
    nb_total_txs =  (txs['total'])
    #Calculate the number of pages for transactions
    print "There are " + str(nb_total_txs)+ " transactions in total on address " + address

    if nb_total_txs%20 ==0:
        nb_pages = nb_total_txs/20
    else:
        nb_pages = nb_total_txs/20 +1
    #print "There are " + str(nb_pages) +  " pages of txs"
    #print nb_pages

    # for x in range(35,nb_pages+1):
    #     txs_on_page = client.address_transactions('1Nb5hT7DqwSHt9uUno68Y4YwDGRnTd36Z8',x)
    #     print len(txs_on_page['data'])















# print(len(client.address_transactions("1dice8EMZmqKvrGE4Qc9bUFf9PX3xaYDp")['data']))
#
# print(client.verify_address("16dwJmR4mX5RguGrocMfN9Q9FR2kZcLw2z", "HPMOHRgPSMKdXrU6AqQs/i9S7alOakkHsJiqLGmInt05Cxj6b/WhS7kJxbIQxKmDW08YKzoFnbVZIoTI2qofEzk="))
#
# # Dealing with numbers
# print("123456789 Satoshi to BTC: ", blocktrail.to_btc(123456789))
# print("1.23456789 BTC to Satoshi: ", blocktrail.to_satoshi(1.23456789))