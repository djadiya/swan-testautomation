# swan-testautomation

From pexepect test get the showmplslsdoutput file:

decodedoutput = pexpectoutput.after.decode()

import sys

with open('showmplslsdoutput', 'w') as sys.stdout:
    print('decodedoutput ')

Run testfsm test which utilizes showmpls.template:
python3 textfsm_module.py


==================

Testing method for logs: Collect part of docker logs corresponding to performaing action.

Used part of docker logs collected to verify action performed based tests.


Taking action ("bash docker restart SwanAgent")
and saving docker logs corresponding to it in /tmp/new/dockerlogs.log on each device:
python3.10 logtestaction2.py

validating test cases on collected docker logs: 
python3.10 validatelogtest2.py

