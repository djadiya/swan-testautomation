# swan-testautomation

From pexepect test get the showmplslsdoutput file:

decodedoutput = pexpectoutput.after.decode()

import sys

with open('showmplslsdoutput', 'w') as sys.stdout:
    print('decodedoutput ')

Run testfsm test which utilizes showmpls.template:
python3 textfsm_module.py

==================

Taking action and saving docker logs corresponding to it in /tmp/new/dockerlogs.log on each device:
python3.10 logtestaction2.py

validating test cases on collected docker logs: 
python3.10 validatelogtest2.py

