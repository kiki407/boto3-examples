# import sys
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import mainconf

(aws_access_key_id, aws_secret_access_key, aws_region) = mainconf.getconfig()
