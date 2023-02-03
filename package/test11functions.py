from logtestlib.logaction import performactionforlogging
from logtestlib.validateactionlogs import validatelogs, validatelogscustextfsmret, validateclicustextfsmret
from logtestlib.readtestbedjson import rnaddrouterobj

def test_verifyslapiservice():
    act = "bash docker restart SwanAgent"
    addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT"],logtag="action")
    performactionforlogging(addrouterobjs,act=act,delaybstoplogging=5)
    
    addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT"],logtag="validation")
    grepstringlist = ["Entered trial 1 for loop process",
            "SL-API server returned SL_INIT_STATE_READY",
            "SL-API heartbeat channel established",
            "TCP connection successfully established",
            "TLS enabled",
            "Finished grabbing LSD labels",
            "Finished obtaining Platform Arch Type",
            "Finished setting handles",
            "Probing initializing",
            "Starting Probe v4 Server"]
    validatelogs(grepstringlist,addrouterobjs,textfsm_template='fixtures/Year')

    grepstringlist2 = ["Entered trial 2 for loop process","Using primary credentials, user:msft"]
    validatelogs(grepstringlist2,addrouterobjs,textfsm_template='fixtures/Year')

    grepstringlist2 = ["checkConnection received error rpc error: code",
            "SL-API client signal error rpc error",
            "Create Client failure: Failed to initialize heartbeat channel with SL-API",
            "Entered trial 3 for loop process",
            "connection error",
            "Router connection error",
            "unable to create a connection to gRPC server"]
    addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT"],logtag="validation-negative")
    validatelogs(grepstringlist2,addrouterobjs,textfsm_template='fixtures/Year')

def test_negtlsenabled():
    grepstringlist3 = ["TLS enabled"]
    addrouterobjs = rnaddrouterobj(["SWAN_MIDPOINT"],logtag="validation-negativei-tlsenabled")
    validatelogs(grepstringlist3,addrouterobjs,textfsm_template='fixtures/Year')
