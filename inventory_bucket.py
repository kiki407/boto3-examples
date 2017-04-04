from boto3.session import Session
aws_id = ""
aws_secret = ""
aws_region = 'eu-west-1'
aws_bucket_name = 'test'

session = Session(
            region_name=aws_region,
            aws_secret_access_key=aws_secret,
            aws_access_key_id=aws_id
            )
s3 = session.client('s3')
paginator = s3.get_paginator('list_objects_v2')

def inventory(bucket):
    pages = paginator.paginate(Bucket=bucket)
    counter = 0
    size = 0
    pages_counter = 0
    for page in pages:
        pages_counter += 1
        counter += len(page['Contents'])
        for obj in page['Contents']:
            size += obj['Size']
    return (pages_counter, counter, sizeof_fmt(size))


inventory(aws_bucket_name)

