#import pyping
from ping3 import ping, verbose_ping
import requests
import time
import os
import socket
import uuid
from getmac import get_mac_address
from mac_vendor_lookup import MacLookup
import ipaddress
import json

#mac = MacLookup()
#mac.update_vendors()
with open("c:\\Users\\cbonb\\OneDrive\\Documents\\Reseaux\\iplist.csv","w") as f:
    f.write("IP,mac,vendor,host,description")
# Read data from file:

dev = {}
#json.dump( dev, open( "iplist.json", 'w' ) )

jsonfile = "c:\\Users\\cbonb\\OneDrive\\Documents\\Reseaux\\iplist1.json"
with open(jsonfile,"r") as f:
    jsonraw = f.read()
    #toskip = json.find("{",0,50)
    #print(json.find("{",0,50))
    rawlist = jsonraw.split("{",1)
    #print(raw[0],"-----------",raw[1])

    jsontxt = "{" + rawlist[1]

with open(jsonfile,"w") as f:
    f.write(jsontxt)
#dev = json.load(json)
dev = json.load( open( jsonfile ))
#print(dev["7c:26:64:87:60:13"]["IP"]," ", dev["7c:26:64:87:60:13"]["vendor"]  ," ", dev["7c:26:64:87:60:13"]["host"]," ", dev["7c:26:64:87:60:13"]["descr"] )
#print(list(dev.keys())[0])



def check(hostname):
    response = ping(hostname,timeout=1)
    print(response)
    print(hostname)
    if response:
            ip_mac = get_mac_address(ip=hostname)
        #with open("iplist.csv", "a") as f:
            try:
                vendeur = MacLookup().lookup(ip_mac)
            except:
                vendeur = "?"
            try:
                host = socket.gethostbyaddr(hostname)
                socket.
            except:
                host = "host?"

            try:
                descr = dev[ip_mac]["descr"]
            except:
                descr = "desc?"

            try:
                with open("c:\\Users\\cbonb\\OneDrive\\Documents\\Reseaux\\iplist.csv", "a") as f:
                    f.write("\n" + hostname + "," +ip_mac+ ","+ vendeur + "," + str(host[0]) + "," + dev[ip_mac] ["descr"])
                #print("dEVICES   " + hostname + "   " +ip_mac+ "   "+ vendeur + "   " + str(host[0])+ "    " + dev[ip_mac] ["descr"] )
            except:
                pass
            try:
                print("dEVICES   " + hostname + "   " + ip_mac + "   " + vendeur + "   " + str(host[0]) + "    " + dev[ip_mac]["descr"])
            except:
                print("dEVICES   " + hostname)
            dev[ip_mac]={ "IP":hostname,  "vendor" : vendeur, "host": str(host[0]), "descr": descr}
            print(dev[ip_mac])
    else:
        pass
i = 0
network = ipaddress.ip_network('192.168.1.0/24')
i = 0
for ip in network :
    if i > 100:
        break
    check(str(ip))
    i += 1
file = open( jsonfile, 'w' )
json.dump( dev,file, indent=4 )
