from logtestlib.logaction import performactionforlogging
from logtestlib.validateactionlogs import validatelogs, validatelogscustextfsmret, validateclicustextfsmret
from logtestlib.readtestbedjson import rnaddrouterobj

def test_example(act="bash docker restart SwanAgent",grepstringlist = ["TLS enabled"], cli="show mpls lsd forwarding labels 24001 detail"):
    addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT","SWAN_PHP"],logtag="action")
    act=act
    performactionforlogging(addrouterobjs,act=act,delaybstoplogging=2)
    addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT","SWAN_PHP"],logtag="validation")
    grepstringlist = grepstringlist 
    validatelogs(grepstringlist,addrouterobjs,textfsm_template='fixtures/Year')
    retcustextfsm = validatelogscustextfsmret(grepstringlist,addrouterobjs,textfsm_template='fixtures/Year')
    print("retvalue -", retcustextfsm)
    retcli = validateclicustextfsmret(cli, addrouterobjs, textfsm_template="fixtures/labels")
    print("retcli -",retcli)

#test_example(act="bash docker restart SwanAgent",grepstringlist = ["TLS enabled"], cli="show mpls lsd forwarding labels 24001 detail")
