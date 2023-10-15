import boto3
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

s3 = boto3.client(
    's3',
    aws_access_key_id=config['aws-credentials']['ACCESS_KEY'],
    aws_secret_access_key=config['aws-credentials']['SECRET_KEY'],    
)

if __name__ == '__main__':
    print('Listing Buckets')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f'    bucket: {bucket["Name"]}')

    print('Upload File')
    response = s3.upload_file('data\\finalizada2020-07.csv', 'thedataengineer-bucket', 'finalizada2020-07.csv')

    print('Listing files')
    response = s3.list_objects(Bucket='thedataengineer-bucket')
    for file in response['Contents']:
        print(file)

    print('Download File')
    s3.download_file('thedataengineer-bucket', 'finalizada2020-07.csv', 'downloaded\\finalizada2020-07.csv')

    print('Delete File')
    s3.delete_object(Bucket='thedataengineer-bucket', Key='finalizada2020-07.csv')

    print('Listing files')
    response = s3.list_objects(Bucket='thedataengineer-bucket')
    print(response)
