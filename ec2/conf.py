# coding: utf8
# add profile details here
import logging

access_key_id = ''
secret_access_key = ''
region = ''

# Or use a config file
conf_file = 'conf.json'
profile = 'default'
'''
Example:
{
    'default': {
        "access_key_id": "AAA...",
        "secret_access_key": "pass...",
        "region": "eu-west-1"
    },
    'dev': {
        "access_key_id": "BBB...",
        "secret_access_key": "pass...",
        "region": "us-east-1"
    },
}
'''


def getconfig(profile='default'):
    if not (access_key_id and secret_access_key and region):
        import json
        try:
            with open(conf_file) as cnf_file:
                conf = json.load(cnf_file)
        except Exception as e:
            logging.error('Could Not Load configuration File')
            logging.debug(e)

    if access_key_id:
        aws_access_key_id = access_key_id
    else:
        aws_access_key_id = conf[profile]['access_key_id']

    if secret_access_key:
        aws_secret_access_key = secret_access_key
    else:
        aws_secret_access_key = conf[profile]['secret_access_key']

    if region:
        aws_region = region
    else:
        aws_region = conf[profile]['region']

    return dict(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_region=aws_region)
