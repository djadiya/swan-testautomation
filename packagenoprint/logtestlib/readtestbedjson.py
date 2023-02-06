from logtestlib.userlib import uname, psword, Addrouter
from logtestlib.logconf import logger
import json
import os

# Below functions create router objects from information passed via testbed.json file
# One could filter creation of router objects based on device names as parameters

#testbedjson = {"platform": "8000", "devices": [{"name": "WAN_INGRESS", "role": "RWA", "ip": "172.23.164.2", "telnetPort": 11275, "sshPort": 63475}, {"name": "SWAN_INGRESS", "role": "OWR", "ip": "172.23.164.2", "telnetPort": 14749, "sshPort": 64934}, {"name": "SWAN_MIDPOINT", "role": "OWR", "ip": "172.23.164.2", "telnetPort": 25841, "sshPort": 61267}, {"name": "SWAN_PHP", "role": "OWR", "ip": "172.23.164.2", "telnetPort": 25079, "sshPort": 64048}, {"name": "SWAN_EGRESS", "role": "OWR", "ip": "172.23.164.2", "telnetPort": 23486, "sshPort": 60970}, {"name": "WAN_EGRESS", "role": "RWA", "ip": "172.23.164.2", "telnetPort": 29438, "sshPort": 61919}, {"name": "ixia_gui", "role": "TGN", "ip": "172.23.164.2", "ixiaPort": 23794}]}

def rntestbedjsongen(testbedjson):
    try:
        genobj = (line for line in testbedjson['devices'] if line['name'] != 'ixia_gui')
    except: 
        logger.exception("Exception from function rntestbedjsongen")
        logger.exception(e)
    return genobj

def rnaddrouterobj(filterlst=[], logtag="action", testbed="../fixtures/testbed.json"):
    try:
        addrouterobjs = []
        currentdir = os.path.dirname(__file__)
        testbedpath = os.path.realpath(os.path.join(currentdir,testbed))
        with open(testbedpath) as f:
            testbedjson = json.load(f)
        o = rntestbedjsongen(testbedjson)
        if filterlst == []:
            filterlst = [line['name'] for line in testbedjson['devices'] if line['name'] != 'ixia_gui']
        else:
            filterlst = filterlst
        for i in o:
            n = 1 
            for m in filterlst:
                unfilteredtuple = (i['ip'],i['sshPort'])
                if m == i['name']:
                    filteredtuple = (i['ip'],i['sshPort'])
                    oname = "cisco" + str(n) + "obj"
                    oname = Addrouter(*filteredtuple, logtag)
                    logger.info("routerobjseq--", oname.objseq)
                    addrouterobjs.append(oname)
                n += 1
    except Exception as e:
        logger.exception("Exception from function rnaddrouterobj")
        logger.exception(e)
    return addrouterobjs

def createconfigjson(inputdict = {}):
    try:
        with open('fixtures/config.json', 'r') as f:
            data = json.load(f)
            logger.info(json.dumps(data, indent=4))
            if inputdict:
                for k in inputdict.keys():
                    data[k]=inputdict[k]

        with open('fixtures/toapplyconfig.json', 'w') as outfile:
            json.dump(data, outfile, ensure_ascii=False)
    except Exception as e:
        logger.exception("Exception from function rcreateconfigjson")
        logger.exception(e)


#obtain all list of router objects by calling without filter parameters
#rnaddrouterobj()
#rnaddrouterobj(["SWAN_MIDPOINT","SWAN_PHP"])
