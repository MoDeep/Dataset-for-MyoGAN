import boto3
import botocore

import shutil
import os

import tarfile

BUCKET_NAME = 'myohand-dataset'
KEY = 'myohand.tar'
output = 'myohand.tar'

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, output)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

curr_path = os.getcwd() + '/'
path = input('Please input download path: ')

print('Moving to ' + path + '...')
shutil.move(os.getcwd() + "\\" + output, path + "\\" + output)
print('Success!')

dataset_tar = tarfile.TarFile(path + "\\" + output)
