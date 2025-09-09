import boto3
 
s3 = boto3.client('s3')

s3.upload_file('sample-data/data.txt', 'my-storage-bucket', 'data.txt')

print("Upload complete!")

