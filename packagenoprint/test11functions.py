from logtestlib.logaction import performactionforlogging
from logtestlib.validateactionlogs import validatelogs, validatelogscustextfsmret, validateclicustextfsmret
from logtestlib.readtestbedjson import rnaddrouterobj
from logtestlib.logconf import logger
import pandas as pd
from datetime import datetime

valrets = []
valrets2 = []

def test_verifyslapiservice():
    act = "bash docker restart SwanAgent"
    addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT"],logtag="action")
    performactionforlogging(addrouterobjs,act=act,delaybstoplogging=5)
    from logtestlib.config import startiso, endiso
    startisonew = pd.to_datetime(startiso, format='%Y-%m-%dT%H:%M:%S.%fZ')
    endisonew = pd.to_datetime(endiso, format='%Y-%m-%dT%H:%M:%S.%fZ')
    addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT"],logtag="validation")
    grepstringlist = ["SWAN Agent version",
            "Entered setConn function",
            "Entered trial 1 for loop process",
            "SL-API server returned SL_INIT_STATE_READY",
            "SL-API heartbeat channel established",
            "TCP connection successfully established",
            "TLS enabled"
            ]
    valret = validatelogscustextfsmret(grepstringlist,addrouterobjs,textfsm_template='fixtures/hmsz')
    [valrets.append(k) for k in valret[2]]
    #validatelogs(grepstringlist,addrouterobjs,textfsm_template='fixtures/Year')
    dtlst = []
    for k in valrets:
        dtlst.append( [pd.to_datetime(k['hmsz'], format='%Y-%m-%dT%H:%M:%S.%fZ'), k['message'].strip()] )

    timea = [k[0] for k in dtlst if k[1] == "TLS enabled"]
    
    if len(timea) == 2:
        timea.sort()
        if timea[0] < timea[1] < endisonew:

            timeb = [k[0] for k in dtlst if k[1] == "SWAN Agent version"]
            timeb.sort()
            if timeb[0] < timea[0]:
                startiso = timeb[0]
            
            time1 = [k[0] for k in dtlst if k[1] == "Entered trial 1 for loop process"]
            time2 = [k[0] for k in dtlst if k[1] == "SL-API server returned SL_INIT_STATE_READY"]
            time3 = [k[0] for k in dtlst if k[1] == "SL-API heartbeat channel established"]
            time4 = [k[0] for k in dtlst if k[1] == "TCP connection successfully established"]
            time1.sort()
            time2.sort()
            time3.sort()
            time4.sort()

            if timea[0] < time1[0] < time2[0] < time3[0] < time4[0] < timea[1] < endisonew:
                logger.info("sliapi connection test passed")
            else:
                logger.info("sliapi connection test failed")

    grepstringlist2 = ["TLS enabled",
            "GME credentials are not available",
            "Entered trial 2 for loop process",
            "Using primary credentials, user:msft",
            "TCP connection successfully established"
            ]
    valret2 = validatelogscustextfsmret(grepstringlist2,addrouterobjs,textfsm_template='fixtures/hmsz')
    [valrets2.append(k) for k in valret2[2]]
    #validatelogs(grepstringlist2,addrouterobjs,textfsm_template='fixtures/Year')
    dtlst2 = []
    for k in valrets2:
        dtlst2.append( [pd.to_datetime(k['hmsz'], format='%Y-%m-%dT%H:%M:%S.%fZ'), k['message'].strip()] )

    time6 =[k[0] for k in dtlst2 if k[1] == "TLS enabled"]
    time7 =[k[0] for k in dtlst2 if k[1] == "GME credentials are not available"]

    if time6[1] < time7[0]:
        startiso = time6[0]

    time8 =[k[0] for k in dtlst2 if k[1] == "Entered trial 2 for loop process"]
    time9 =[k[0] for k in dtlst2 if k[1] == "Using primary credentials, user:msft"]
    time10 =[k[0] for k in dtlst2 if k[1] == "TCP connection successfully established"]
    time6.sort()
    time7.sort()
    time8.sort()
    time9.sort()
    time10.sort()

    if startiso < time6[1] < time7[0] < time8[0] < time9[0] < time10[1] < endisonew:
        logger.info("yang connection test passed")
    else:
        logger.info("yang connection test failed")

    
