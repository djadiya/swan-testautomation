import logging
import sys, getopt
from test_tlsenabled_example import test_example
from test11functions import test_verifyslapiservice, test_negtlsenabled

def main(argv):

    logging.basicConfig(level=logging.INFO)

    try:
        opts, args = getopt.getopt(argv,"hi",["itestbed="])
        for opt, arg in opts:
            if opt == '-h':
                logging.info('test8 -i <testbed>')
                sys.exit()
            elif opt in ("-i", "--itestbed"):
                testbedFile = args[0]

        testbed = open(testbedFile)
        readtestbed = testbed.read()
        #print(readtestbed)
        with open('fixtures/testbed.json', 'w') as f:
            f.write(readtestbed)

    except getopt.GetoptError as e:
        logging.exception("Exception msg:"+str(e))
    except Exception as e:
        logging.exception("Exception msg:"+str(e))

if __name__ == "__main__":
    main(sys.argv[1:])
    #test_verifyslapiservice()
    test_negtlsenabled()
