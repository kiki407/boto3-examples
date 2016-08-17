import conf
import logging
from boto3.session import Session
import pprint

session = Session(
    aws_access_key_id=conf.aws_access_key_id,
    aws_secret_access_key=conf.aws_secret_access_key,
    region_name=conf.aws_region)


def listimages(os='', arch='', amazononly=False, virtype=''):
    ec2 = session.client('ec2')
    filters = []

    filters.append(
            {
                'Name': 'state',
                'Values': ['available']
            }
        )

    if virtype.lower() == 'hvm':
        filters.append(
            {
                'Name': 'virtualization-type',
                'Values': [virtype.lower()]
            }
        )
    elif virtype.lower() == 'paravirtual':
        filters.append(
            {
                'Name': 'virtualization-type',
                'Values': [virtype.lower()]
            }
        )

    if amazononly:
        filters.append(
            {
                'Name': 'owner-alias',
                'Values': ['amazon']
            }
        )

    if os.lower() == 'windows':
        filters.append(
            {
                'Name': 'platform',
                'Values': [os.lower()]
            }
        )

    if arch.lower() == 'i386':
        filters.append(
            {
                'Name': 'platform',
                'Values': [os.lower()]
            }
        )
    elif arch.lower() == 'x86_64':
        filters.append(
            {
                'Name': 'platform',
                'Values': [os.lower()]
            }
        )

    amis = ec2.describe_images(
        # Owners=[conf.aws_owner_id],
        Filters=filters
        # Filters=[{'Name': 'name', 'Values': ['sciforma-generic-tmp-enc', 'sciforma']}]
        )

    _amis = pprint.pformat(amis['Images'])
    return amis['Images']

if '__main__' == __name__:
    amis = listimages(
        # os='windows',
        # arch='i386',
        # amazononly=True,
        virtype='hvm'
        )

    # Reduce list to ubuntu only
    ubuntu_list = filter(lambda x: 'Name' in x.keys() and 'ubuntu' in x['Name'], amis)

    # Reduce list to amazon-ami only
    amazon_list = filter(lambda x: 'Name' in x.keys() and 'amazon' in x['Name'], amis)

    logging.info(pprint.pformat(ubuntu_list))
    logging.info(pprint.pformat(amazon_list))
    logging.info(len(amis))
