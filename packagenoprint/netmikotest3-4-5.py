from logtestlib.readtestbedjson import rnaddrouterobj

def validatetest03(rtrnode="SWAN_MIDPOINT", interfacename="Gi 2", label=24001):

    addrouterobjs = rnaddrouterobj([rtrnode],logtag="validation-test03")

    addrouterobjs[0].rtrconnhandle.enable()
    addrouterobjs[0].rtrconnhandle.config_mode()
    addrouterobjs[0].rtrconnhandle.send_config_set(['interface '+ interfacename, 'shut','commit','end'])
    res1 = addrouterobjs[0].rtrconnhandle.send_command('show mpls lsd forwarding labels '+ label, use_textfsm=True, textfsm_template="fixtures/labels.template")

    addrouterobjs[0].rtrconnhandle.enable()
    addrouterobjs[0].rtrconnhandle.config_mode()
    addrouterobjs[0].rtrconnhandle.send_config_set(['interface '+ interfacename, 'no shut','commit','end'])
    res2 = addrouterobjs[0].rtrconnhandle.send_command('show mpls lsd forwarding labels '+ label, use_textfsm=True, textfsm_template="fixtures/labels.template")


def validatetest04(rtrnode="SWAN_MIDPOINT", interfacename="Bundle-Ether 2", label=24001):

    addrouterobjs = rnaddrouterobj([rtrnode],logtag="validation-test04")

    addrouterobjs[0].rtrconnhandle.enable()
    addrouterobjs[0].rtrconnhandle.config_mode()
    addrouterobjs[0].rtrconnhandle.send_config_set(['interface '+ interfacename, 'shut','commit','end'])
    res1 = addrouterobjs[0].rtrconnhandle.send_command('show mpls lsd forwarding labels '+ label, use_textfsm=True, textfsm_template="fixtures/labels.template")

    addrouterobjs[0].rtrconnhandle.enable()
    addrouterobjs[0].rtrconnhandle.config_mode()
    addrouterobjs[0].rtrconnhandle.send_config_set(['interface '+ interfacename, 'no shut','commit','end'])
    res2 = addrouterobjs[0].rtrconnhandle.send_command('show mpls lsd forwarding labels '+ label, use_textfsm=True, textfsm_template="fixtures/labels.template")

def validatetest05(rtrnode="SWAN_MIDPOINT", label=24001):

    addrouterobjs = rnaddrouterobj([rtrnode],logtag="validation-test05")

    addrouterobjs[0].rtrconnhandle.enable()
    addrouterobjs[0].rtrconnhandle.config_mode()
    addrouterobjs[0].rtrconnhandle.send_config_set(['no router isis 1','commit','end'])
    res1 = addrouterobjs[0].rtrconnhandle.send_command('show mpls lsd forwarding labels '+ label, use_textfsm=True, textfsm_template="fixtures/labels.template")

    addrouterobjs[0].rtrconnhandle.enable()
    addrouterobjs[0].rtrconnhandle.config_mode()
    addrouterobjs[0].rtrconnhandle.send_config_set(['router isis 1',
        'is-type lee-2-only',
        'net 49.0901.0000.0000.0002.00',
        'distribute link-state level 2',
        'address-family ipv4 unicast',
        'metric-style wide',
        'advertise link attributes',
        'mpls traffic-eng level-2-only',
        'mpls traffic-eng router-id Loopback99',
        'maximum-paths 32',
        'segment-routing mpls',
        'segment-routing prefix-sid-map advertise-local',
        'address-family ipv6 unicast',
        'metric-style wide',
        'advertise link attributes',
        'router-id Loopback99',
        'single-topology',
        'redistribute connected',
        'maximum-paths 32',
        'segment-routing mpls',
        'segment-routing prefix-sid-map advertise-local',
        'interface Loopback99',
        'address-family ipv4 unicast',
        'address-family ipv6 unicast',
        'interface Bundle-Ether 1',
        'circuit-type level-2-only',
        'point-to-point',
        'address-family ipv4 unicast',
        'address-family ipv6 unicast',
        'interface Bundle-Ether 2',
        'circuit-type level-2-only',
        'point-to-point',
        'address-family ipv4 unicast',
        'address-family ipv6 unicast',
        'commit',
        'end'])
    res2 = addrouterobjs[0].rtrconnhandle.send_command('show mpls lsd forwarding labels '+ label, use_textfsm=True, textfsm_template="fixtures/labels.template")
