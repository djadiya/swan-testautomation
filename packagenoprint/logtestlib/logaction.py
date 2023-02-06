from netmiko  import (NetMikoAuthenticationException, NetMikoTimeoutException)
from logtestlib.readtestbedjson import rnaddrouterobj
from time import sleep,time
from datetime import datetime
import pandas as pd
from logtestlib.logconf import logger
import logtestlib.config as config 

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
    #commandstart3 = "bash a=`date +%s` && sincedate=$(date -I -d @`echo $a`) && docker restart SwanAgent && docker logs --since $sincedate -t SwanAgent > /tmp/new/dockerlogs2.log"
    #commandend = "bash fuser -k /tmp/new/dockerlogs2.log"
    #commandstart3 = "bash docker ps -a"
    #commandend = "bash docker ps -a"
    
    for device in addrouterobjs:
        try: 
            outputstart2 = device.sndcmd(commandstart2)
            logger.info(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
            logger.info("=" * 2 * len(device.netmiko_connect.host))
            logger.info(outputstart2)
            logger.info("")
            #outputstart3 = device.sndcmd(commandstart3)
            #print(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
            #print("=" * 2 * len(device.netmiko_connect.host))
            #print(outputstart3)
            #print()
        except NetMikoTimeoutException:
            logger.exception("Device Unreachable from performactionforlogging")
        except Exception as e:
            logger.exception("Exception from performactionforlogging")
            logger.exception(e)
    config.startiso = pd.to_datetime('now') + pd.Timedelta(111) 
    logger.info("START ", config.startiso)
    start = time()
    commandaction = "bash docker restart SwanAgent" 
    try:
        outputaction = addrouterobjs[0].sndcmd(commandaction, delay_factor=10)
        logger.info(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
        logger.info("=" * 2 * len(device.netmiko_connect.host))
        logger.info(outputaction)
        logger.info("")
    except NetMikoTimeoutException:
        logger.exception("Device Unreachable from performactionforlogging commandaction")
    except Exception as e:
        logger.exception("Exception from performactionforlogging commandaction")
        logger.exception(e)
    
    sleep(delaybstoplogging)    

    for device in addrouterobjs:
        try:
            end = time()
            sincetimeinseconds = int(end-start) + 2
            commandend = "bash docker logs -t --since "+str(sincetimeinseconds)+"s SwanAgent > /tmp/new/dockerlogs2.log 2>&1 &"
            outputend = device.sndcmd(commandend)
            config.endiso = pd.to_datetime('now') + pd.Timedelta(111)
            logger.info("END ",  config.endiso)
            logger.info(commandend)
            logger.info(device.netmiko_connect.host,"  ",device.netmiko_connect.port)
            logger.info("=" * 2 * len(device.netmiko_connect.host))
            logger.info(outputend)
            logger.info("")
        except NetMikoTimeoutException:
            logger.exception("Device Unreachable from performactionforlogging commandend")
        except Exception as e:
            logger.exception("Exception from performactionforlogging commandend")
            logger.exception(e)
