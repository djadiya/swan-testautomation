from netmiko import ConnectHandler
from netmiko  import (NetMikoAuthenticationException, NetMikoTimeoutException)
from logtestlib.readtestbedjson import rnaddrouterobj
from logtestlib.logconf import logger
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
                logger.info(commandgrep)
                outputgrep = device.sndcmd(commandgrep, use_textfsm=True, textfsm_template=textfsm_template)
                logger.info(device.netmiko_connect.host,"  ",device.netmiko_connect.port," ","objseq - ",device.objseq)
                logger.info("=" * 2 * len(device.netmiko_connect.host))
                if (type(outputgrep[0]) is dict):
                        if (str(outputgrep[0]['year']) == yr):
                            logger.info(grepstring + " TEST_PASSED")
                            logger.info(outputgrep)
                        else:
                            logger.info(grepstring + " TEST_FAILED for missing grepstring")
                            logger.info(outputgrep)
                else:
                    logger.info(grepstring + " TEST_FAILED for not returning a dict")
                    logger.info(outputgrep)
                logger.info("")
            except NetMikoTimeoutException:
                logger.exception("Device Unreachable from validatelogs")
            except Exception as e:
                logger.exception("Excepion from validatelogs")
                logger.exception(e)

def validatelogscustextfsmret(grepstringlist=grepstringlist,addrouterobjs="addrouterobjs",textfsm_template="customyearerr.template"):
    retobj = {}
    for device in addrouterobjs:
        for grepstring in grepstringlist:
            try:
                commandgrep = "bash cat /tmp/new/dockerlogs2.log | grep -i '" + grepstring + "' | head -2"
                logger.info(commandgrep)
                outputgrep = device.sndcmd(commandgrep, use_textfsm=True, textfsm_template=textfsm_template)
                logger.info(device.netmiko_connect.host,"  ",device.netmiko_connect.port," ","objseq - ",device.objseq)
                logger.info("=" * 2 * len(device.netmiko_connect.host))
                if len(outputgrep) > 1 :
                    outputgrep[0]['message'] = grepstring
                    outputgrep[1]['message'] = grepstring
                outputgrep[0]['message'] = grepstring
                logger.info(outputgrep)
                if device.objseq in retobj:
                    retobj[device.objseq] += outputgrep 
                else:
                    retobj[device.objseq] = outputgrep
            except NetMikoTimeoutException:
                logger.exception("Device Unreachable from function validatelogscustextfsmret")
            except Exception as e:
                logger.exception("Exception from function validatelogscustextfsmret")
                logger.exception(e)
    return retobj

def validateclicustextfsmret(cli="show mpls lsd forwarding labels 24001 detail",addrouterobjs="addrouterobjs",textfsm_template="customcli.template"):
    commandcust = cli
    custextfsmret = {}
    for device in addrouterobjs:
        try:
            outputcust = device.sndcmd(commandcust, use_textfsm=True, textfsm_template=textfsm_template)
            logger.info(device.netmiko_connect.host,"  ",device.netmiko_connect.port," ","objseq - ",device.objseq)
            logger.info("=" * 2 * len(device.netmiko_connect.host))
            custextfsmret[device.objseq]=outputcust
        except NetMikoTimeoutException:
            logger.exception("Device Unreachable from validateclicustextfsmret")
        except Exception as e:
            logger.exception("Exception from validateclicustextfsmret")
            logger.exception(e)
    return custextfsmret 

def validatecli(cli="show mpls lsd forwarding labels 24001 detail",addrouterobjs="addrouterobjs",textfsm_template="labels"):
    commandmpls = cli
    for device in addrouterobjs:
        try:
            outputmpls = device.sndcmd(commandmpls, use_textfsm=True, textfsm_template="labels")
            logger.info(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
            logger.info("=" * 2 * len(device.netmiko_connect.host))
            if type(outputgrep[0]) is dict:
                if outputmpls[0][textfsm_tmplate] == '':
                    logger.info(commandmpls + " TEST_PASSED")
            else:
                logger.info(commandmpls + " TEST_FAILED")
            logger.info("")
        except NetMikoTimeoutException:
            logger.exception("Device Unreachable from validatecli")
        except Exception as e:
            logger.exception("Exception from validatecli")
            logger.exception(e)

