from netmiko import ConnectHandler
from netmiko  import (NetMikoAuthenticationException, NetMikoTimeoutException)
from logtestlib.readtestbedjson import rnaddrouterobj
import datetime
today = datetime.date.today()
yr = today.strftime("%Y")
import re

#cisco1obj = Addrouter("172.23.164.9", "60585")
#cisco2obj = Addrouter("172.23.164.9", "60438")
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

#addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT","SWAN_PHP"], logtag="validation")
#print("routerobjs -- ", addrouterobjs)

def validatelogs(grepstringlist=grepstringlist,addrouterobjs="addrouterobjs",textfsm_template='Year'):
    for device in addrouterobjs:
        for grepstring in grepstringlist:
            try:
                commandgrep = "bash cat /tmp/new/dockerlogs2.log | grep -i '" + grepstring + "' | head -2"
                print(commandgrep)
                outputgrep = device.sndcmd(commandgrep, use_textfsm=True, textfsm_template=textfsm_template)
                print(device.netmiko_connect.host,"  ",device.netmiko_connect.port," ","objseq - ",device.objseq)
                print("=" * 2 * len(device.netmiko_connect.host))
                if (type(outputgrep[0]) is dict):
                        if (str(outputgrep[0]['year']) == yr):
                            print(grepstring + " TEST_PASSED")
                            print(outputgrep)
                        else:
                            print(grepstring + " TEST_FAILED for missing grepstring")
                            print(outputgrep)
                else:
                    print(grepstring + " TEST_FAILED for not returning a dict")
                    print(outputgrep)
                print()
            except NetMikoTimeoutException:
                print("Device Unreachable from validatelogs")
            except Exception as e:
                print("Excepion from validatelogs")
                print(e)

def validatelogscustextfsmret(grepstringlist=grepstringlist,addrouterobjs="addrouterobjs",textfsm_template="customyearerr.template"):
    retobj = {}
    for device in addrouterobjs:
        for grepstring in grepstringlist:
            try:
                commandgrep = "bash cat /tmp/new/dockerlogs2.log | grep -i '" + grepstring + "' | head -2"
                print(commandgrep)
                outputgrep = device.sndcmd(commandgrep, use_textfsm=True, textfsm_template=textfsm_template)
                print(device.netmiko_connect.host,"  ",device.netmiko_connect.port," ","objseq - ",device.objseq)
                print("=" * 2 * len(device.netmiko_connect.host))
                print(outputgrep)
                retobj[device.objseq]=outputgrep 
            except NetMikoTimeoutException:
                print("Device Unreachable from function validatelogscustextfsmret")
            except Exception as e:
                print("Exception from function validatelogscustextfsmret")
                print(e)
    return retobj

def validateclicustextfsmret(cli="show mpls lsd forwarding labels 24001 detail",addrouterobjs="addrouterobjs",textfsm_template="customcli.template"):
    commandcust = cli
    custextfsmret = {}
    for device in addrouterobjs:
        try:
            outputcust = device.sndcmd(commandcust, use_textfsm=True, textfsm_template=textfsm_template)
            print(device.netmiko_connect.host,"  ",device.netmiko_connect.port," ","objseq - ",device.objseq)
            print("=" * 2 * len(device.netmiko_connect.host))
            custextfsmret[device.objseq]=outputcust
        except NetMikoTimeoutException:
            print("Device Unreachable from validateclicustextfsmret")
        except Exception as e:
            print("Exception from validateclicustextfsmret")
            print(e)
    return custextfsmret 

def validatecli(cli="show mpls lsd forwarding labels 24001 detail",addrouterobjs="addrouterobjs",textfsm_template="labels"):
    commandmpls = cli
    for device in addrouterobjs:
        try:
            outputmpls = device.sndcmd(commandmpls, use_textfsm=True, textfsm_template="labels")
            print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
            print("=" * 2 * len(device.netmiko_connect.host))
            if type(outputgrep[0]) is dict:
                if outputmpls[0][textfsm_tmplate] == '':
                    print(commandmpls + " TEST_PASSED")
            else:
                print(commandmpls + " TEST_FAILED")
            print()
        except NetMikoTimeoutException:
            print("Device Unreachable from validatecli")
        except Exception as e:
            print("Exception from validatecli")
            print(e)

