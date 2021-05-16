def lambda_handler(event, context):
s3 = boto3.client('s3', use_ssl = False)

s3.upload_fileobj(
    Fileobj = gzip.GzipFile(
        None,
        'rb',
        fileobj = BytesIO(
            s3.get_object(Bucket='bucketName', Key='key')['Body'].read())),
            Bucket ='bucketName',
            Key ='key')
