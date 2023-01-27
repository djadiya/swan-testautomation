from netmiko import ConnectHandler
from netmiko  import (NetMikoAuthenticationException, NetMikoTimeoutException)
from readtestbedjson import rnaddrouterobj

# use below steps to create ip, port based router objects in test case file
#from userlib import uname, psword, Addrouter
#cisco1obj = Addrouter("172.23.164.9", "60585")
#cisco2obj = Addrouter("172.23.164.9", "60438")

# use below call without any parameter to get all possible router objects from testbed.json file
#addrouterobjs = rnaddrouterobj()

addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT","SWAN_PHP"])
print("routerobjs -- ", addrouterobjs)

commandstart2 = "bash mkdir -p /tmp/new"
commandstart3 = "bash docker logs -f -t  SwanAgent > /tmp/new/dockerlogs2.log 2>&1 &"
commandinbetween = "show ip int brief"
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
        outputinbetween = device.sndcmd(commandinbetween)
        print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
        print("=" * 2 * len(device.netmiko_connect.host))
        print(outputinbetween)
        print()
    except NetMikoTimeoutException:
        print("Device Unreachable")
    except Exception as e:
        print(e)

commandinbetween2 = "bash docker restart SwanAgent"
try:
    output = addrouterobjs[0].sndcmd(commandinbetween2, delay_factor=10)
    print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
    print("=" * 2 * len(device.netmiko_connect.host))
    print(output)
    print()
except NetMikoTimeoutException:
    print("Device Unreachable")
except Exception as e:
        print(e)

for device in addrouterobjs:
    try:
        outputend = device.sndcmd(commandend)
        print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
        print("=" * 2 * len(device.netmiko_connect.host))
        print(outputend)
        print()
    except NetMikoTimeoutException:
        print("Device Unreachable")
    except Exception as e:
        print(e)
