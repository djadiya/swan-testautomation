# swan-testautomation

From pexepect test get the showmplslsdoutput file:

decodedoutput = pexpectoutput.after.decode()

import sys

with open('showmplslsdoutput', 'w') as sys.stdout:
    print('decodedoutput ')

Run testfsm test which utilizes showmpls.template:
python3 textfsm_module.py
