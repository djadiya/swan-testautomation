from logtestlib.userlib import uname, psword, Addrouter

# Below functions create router objects from information passed via testbed.json file
# One could filter creation of router objects based on device names as parameters

testbedjson = {"platform": 9000, "devices": [{"name": "WAN_EGRESS", "role": "", "ip": "172.26.228.190", "telnetPort": 10974, "sshPort": 60524}, {"name": "SWAN_EGRESS", "role": "", "ip": "172.26.228.190", "telnetPort": 12190, "sshPort": 63756}, {"name": "SWAN_PHP", "role": "", "ip": "172.23.164.2", "telnetPort": 20452, "sshPort": 60420}, {"name": "SWAN_MIDPOINT", "role": "", "ip": "172.23.164.2", "telnetPort": 18381, "sshPort": 62245}, {"name": "SWAN_INGRESS", "role": "", "ip": "172.23.164.2", "telnetPort": 23026, "sshPort": 64934}, {"name": "WAN_INGRESS", "role": "", "ip": "172.26.228.190", "telnetPort": 19020, "sshPort": 61793}]}

def rntestbedjsongen(testbedjson):
    genobj = (line for line in testbedjson['devices'])
    return genobj
def rnaddrouterobj(filterlst=[], logtag="action", testbedjson=testbedjson):
    addrouterobjs = []
    o = rntestbedjsongen(testbedjson)
    if filterlst == []:
        filterlst = [line['name'] for line in testbedjson['devices']]
    else:
        filterlst = filterlst
    for i in o:
        n = 1
        for m in filterlst:
            if m is i['name']:
                filteredtuple = (i['ip'],i['sshPort'])
                oname = "cisco" + str(n) + "obj"
                oname = Addrouter(*filteredtuple, logtag)
                print("routerobjseq--", oname.objseq)
                addrouterobjs.append(oname)
            n += 1
    return addrouterobjs

#obtain all list of router objects by calling without filter parameters
#rnaddrouterobj()
#rnaddrouterobj(["SWAN_MIDPOINT","SWAN_PHP"])

