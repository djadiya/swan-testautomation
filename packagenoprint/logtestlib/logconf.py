import logging
import os


currentdir = os.path.dirname(__file__)
logfilepath = os.path.realpath(os.path.join(currentdir,"../fixtures/framework.log"))

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    handlers = [
                        logging.FileHandler(logfilepath),
                        logging.StreamHandler()
                        ])

logging.info("netmiko framwork logging")

logger = logging.getLogger('netmiko framework logging')
