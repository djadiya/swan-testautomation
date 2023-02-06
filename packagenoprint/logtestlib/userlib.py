from netmiko import ConnectHandler, file_transfer
from netmiko import (NetMikoAuthenticationException, NetMikoTimeoutException)
from logtestlib.logconf import logger
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
            "username": uname,
            "password": psword,
            "port": self.prt,
            "fast_cli": False,
            "global_delay_factor": 2.0,
            "session_log": "logtestlogs/" + ip +'-'+ str(self.prt) +'-'+ self.logtag + str(self.objseq) +'-netmiko_session.log',
        }
        try:
            self.netmiko_connect = ConnectHandler(**cisco_ios)
        except NetMikoAuthenticationException:
            logger.exception("Authentication Failed from Addrouter")
        except Exception as e:
            logger.exception("Exception from Addrouter")
            logger.exception(e)

    def sndcmd(self, instruct, **kwargs):
        try:
            res = self.netmiko_connect.send_command(instruct, **kwargs)
            time.sleep(1)
            return res
        except Exception as e:
            logger.exception("Exception from Addrouter sndcmd")
            logger.exception(e)

    def transfiletortr(self, source_file="fixtures/toapplyconfig.json", dest_file="desttoapplyconfig.json", dest_dironrtr=None, dest_fileonrtr=None):
        try:
            filesystem = "/misc/scratch"
            transfer_dict = file_transfer(
                    self.netmiko_connect,
                    source_file=source_file,
                    dest_file=dest_file,
                    file_system=filesystem,
                    # use direction="get" to obtain file from router
                    direction="put",
                    overwrite_file=True,
                    disable_md5=True,
                    )
            transfer_result = all(v for k,v in transfer_dict.items() if k in ["file_transferred","file_exists"]) 
            if transfer_result:
                if dest_dironrtr != None:
                    if dest_fileonrtr != None:
                        outputmv = self.sndcmd("bash mv "+filesystem+"/"+dest_file+" "+dest_dironrtr+"/"+dest_fileonrtr)
                    else:
                        logger.info("dest_fileonrtr not provided")
                else:
                    logger.info("dest_dironrtr not provided")
            else:
                logger.info("file transfer failed: ", transfer_dict)

            logger.info(transfer_dict)
            logger.info("outputmv" ,outputmv)
            return transfer_dict
        except Exception as e:
            logger.exception("Exception from Addrouter transfiletortr")
            logger.exception(e)

    def rtrconnhandle(self):
            return self.netmiko_connect
