from logtestlib.logaction import performactionforlogging
from logtestlib.validateactionlogs import validatelogs, validatelogscustextfsmret, validateclicustextfsmret
from logtestlib.readtestbedjson import rnaddrouterobj, createconfigjson
from logtestlib.userlib import transfiletortr
from logtestlib.userlib import uname, psword, Addrouter

def verifygrpc():
    act = "bash docker restart SwanAgent"
    addrouterobjs = rnaddrouterobj(["SWAN_EGRESS"],logtag="action")
    performactionforlogging(addrouterobjs,act=act,delaybstoplogging=5)
    addrouterobjs = rnaddrouterobj(["SWAN_EGRESS"],logtag="validation")
    grepstringlist = ["Using primary credentials"]
    validatelogs(grepstringlist,addrouterobjs,textfsm_template='fixtures/Year')
    with open('fixtures/inputconfig1.json', 'r') as f:
        m = json.load(f)
    createconfigjson(m)
    addrouterobjs[0].transfiletortr(dest_dironrtr="/var/lib/docker/appmgr/config/swanagent/",dest_fileonrtr="config.json")
    performactionforlogging(addrouterobjs,act=act,delaybstoplogging=5)
    grepstringlist2 = ["Using backup credentials, user:msft","Check gRPC connection for IOSXR(YANG) using TCP with different credentials:"]
    validatelogs(grepstringlist2,addrouterobjs,textfsm_template='fixtures/Year')

    addrouterobjs[0].transfiletortr("fixtures/config.json","config.json",dest_dironrtr="/var/lib/docker/appmgr/config/swanagent/",dest_fileonrtr="config.json")

    performactionforlogging(addrouterobjs,act=act,delaybstoplogging=5)


