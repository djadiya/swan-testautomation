from netmiko import ConnectHandler
from netmiko  import (NetMikoAuthenticationException, NetMikoTimeoutException)
from readtestbedjson import rnaddrouterobj
import datetime
today = datetime.date.today()
yr = today.strftime("%Y")
import re

#cisco1obj = Addrouter("172.23.164.9", "60585")
#cisco2obj = Addrouter("172.23.164.9", "60438")

addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT","SWAN_PHP"], logtag="validation")
print("routerobjs -- ", addrouterobjs)

grepstringlist = ['Starting Probe v6 Server', 
                  'Starting Probe v4 Server',
                  'Finished updating interface map',
                  'Finished obtaining interface LACP statuses',
                  'Finished obtaining interface MAC Map',
                  'Finished obtaining interface statuses',
                  'Finished obtaining Platform Arch Type',
                  'h.maxPrimaryPathPerEntry',
                  'maxIPv4RoutePerRouteMsg',
                  'maxIPv6RoutePerRouteMsg',
                  'Skipping init of Pop and Recirc due to prior labels in LSD',
                  'Finished grabbing LSD labels',
                  'Retrieving LSD to check for prior labels',
                  'Max entries and paths per ILM',
                  'have a valid CBF config',
                  'checkConnection received error',
                  'Established connection with gRPC server',
                  'Attempt UNIX connection',
                  'TLS enabled',
                  'Router connection error',
                  'Using backup credentials',
                  'Using primary credentials',
                  'restart exponential back off policy'
                  ]

for device in addrouterobjs:
    for grepstring in grepstringlist:
        try:
            commandgrep = "bash cat /tmp/new/dockerlogs2.log | grep -i '" + grepstring + "' | head -2"
            print(commandgrep)
            outputgrep = device.sndcmd(commandgrep, use_textfsm=True, textfsm_template="showmpls4.template")
            print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
            print("=" * 2 * len(device.netmiko_connect.host))
            if (type(outputgrep[0]) is dict):
                    if ((str(outputgrep[0]['year']) == yr)  and (outputgrep[0]['err'] == '')):
                        print(grepstring + " TEST_PASSED")
                        print(outputgrep)
                    else:
                        if outputgrep[0]['err'] != '':
                            print(grepstring + " TEST_FAILED with ERRO")
                            print(outputgrep)
                        else:
                            print(grepstring + " TEST_FAILED for missing grepstring")
                            print(outputgrep)
            else:
                print(grepstring + " TEST_FAILED for not returning a dict")
                print(outputgrep)
        except NetMikoTimeoutException:
            print("Device Unreachable")
        except Exception as e:
            print(e)

commandmpls = "show mpls lsd forwarding labels 24001 detail"

for device in addrouterobjs:
    try:
        outputmpls = device.sndcmd(commandmpls, use_textfsm=True, textfsm_template="showmpls.template")
        print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
        print("=" * 2 * len(device.netmiko_connect.host))
        if type(outputgrep[0]) is dict:
            if outputmpls[0]['labels'] == '':
                print(commandmpls + " TEST_PASSED")
        else:
            print(commandmpls + " TEST_FAILED")
        print()
    except NetMikoTimeoutException:
        print("Device Unreachable")
    except Exception as e:
        print(e)

