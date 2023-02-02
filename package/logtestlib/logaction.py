from netmiko import ConnectHandler
from netmiko  import (NetMikoAuthenticationException, NetMikoTimeoutException)
from logtestlib.readtestbedjson import rnaddrouterobj
from time import sleep

# use below steps to create ip, port based router objects in test case file
#from userlib import uname, psword, Addrouter
#cisco1obj = Addrouter("172.23.164.9", "60585")
#cisco2obj = Addrouter("172.23.164.9", "60438")

# use below call without any parameter to get all possible router objects from testbed.json file
#addrouterobjs = rnaddrouterobj()

#addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT","SWAN_PHP"], logtag="action")
#print("routerobjs -- ", addrouterobjs)

def performactionforlogging(addrouterobjs="addrouterobjs",act="bash docker restart SwanAgent",delaybstoplogging=10):

    commandstart2 = "bash mkdir -p /tmp/new && touch /tmp/new/dockerlogs2.log && > /tmp/new/dockerlogs2.log"
    commandstart3 = "bash docker logs -f --since 0m -t SwanAgent > /tmp/new/dockerlogs2.log 2>&1 &"
    commandend = "bash fuser -k /tmp/new/dockerlogs2.log"
    
    for device in addrouterobjs:
        try: 
            outputstart2 = device.sndcmd(commandstart2)
            print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
            print("=" * 2 * len(device.netmiko_connect.host))
            print(outputstart2)
            print()
            outputstart3 = device.sndcmd(commandstart3)
            print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
            print("=" * 2 * len(device.netmiko_connect.host))
            print(outputstart3)
            print()
        except NetMikoTimeoutException:
            print("Device Unreachable from performactionforlogging")
        except Exception as e:
            print("Exception from performactionforlogging")
            print(e)
    
    commandaction = act 
    try:
        outputaction = addrouterobjs[0].sndcmd(commandaction, delay_factor=10)
        print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
        print("=" * 2 * len(device.netmiko_connect.host))
        print(outputaction)
        print()
    except NetMikoTimeoutException:
        print("Device Unreachable from performactionforlogging commandaction")
    except Exception as e:
        print("Exception from performactionforlogging commandaction")
        print(e)
    
    sleep(delaybstoplogging)    

    for device in addrouterobjs:
        try:
            outputend = device.sndcmd(commandend)
            print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
            print("=" * 2 * len(device.netmiko_connect.host))
            print(outputend)
            print()
        except NetMikoTimeoutException:
            print("Device Unreachable from performactionforlogging commandend")
        except Exception as e:
            print("Exception from performactionforlogging commandend")
            print(e)
