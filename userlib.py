from netmiko import ConnectHandler
from netmiko  import (NetMikoAuthenticationException, NetMikoTimeoutException)
#from getpass import getpass
import time

uname = "cisco"
psword = "cisco123"

#use getpass, if one does not want to keep passwords in test case files
#psword = getpass.getpass('Please enter the router password: ')

class Addrouter():
    objseq = 0
    def __init__(self, ip=None, prt=None, logtag="action"):
        self.ip = ip
        self.prt = prt
        Addrouter.objseq+=1
        self.objseq=Addrouter.objseq
        self.logtag=logtag
        cisco_ios = {
            "device_type":"cisco_ios",
            "host": self.ip,
            "username": "cisco",
            "password": "cisco123",
            "port": self.prt,
            "fast_cli": False,
            "global_delay_factor": 2.0,
            "session_log": ip +'-'+ str(self.prt) +'-'+ self.logtag + str(self.objseq) +'-netmiko_session.log',
        }
        try:
            self.netmiko_connect = ConnectHandler(**cisco_ios)
        except NetMikoAuthenticationException:
            print("Authentication Failed")
        except Exception as e:
            print(e)

    def sndcmd(self, instruct, **kwargs):
        try:
            res = self.netmiko_connect.send_command(instruct, **kwargs)
            time.sleep(1)
            return res
        except Exception as e:
            print(e)
