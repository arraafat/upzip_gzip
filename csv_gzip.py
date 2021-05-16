import json
import csv
import gzip
import boto3
import zipfile
from io import BytesIO
#https://medium.com/@johnpaulhayes/how-extract-a-huge-zip-file-in-an-amazon-s3-bucket-by-using-aws-lambda-and-python-e32c6cf58f06
#https://stackoverflow.com/questions/55018973/unzip-file-from-s3-write-to-a-csv-file-and-push-back-to-s3

def lambda_handler(event, context):
    s3 = boto3.client('s3', use_ssl = False)
    s3.upload_fileobj(Fileobj = gzip.GzipFile(None,'rb',
        fileobj = BytesIO(
                s3.get_object(Bucket='<Your bucket name >', Key='<Your file prefix>')['Body'].read())),
                Bucket ='<Your output bucket name>',
                Key ='Your file prefix.csv')
