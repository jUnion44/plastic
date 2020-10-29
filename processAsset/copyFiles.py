
import boto3, sys

fileName = sys.argv[1]
fileAccName = sys.argv[2]
session = boto3.session.Session()
client = session.client('s3',
                        region_name='sfo2',
                        endpoint_url='https://sfo2.digitaloceanspaces.com',
                        aws_access_key_id="POTR4I5FSNCEF3OUGSV5",
                        aws_secret_access_key="3aJaqDuBbwfBEME41ILK7zJuNxYZH/64I97g2X3xp7M")
client.put_object(Bucket='plastic',
                    Key=fileName.split("/")[-1],
                    Body=open(fileName,"rb").read(),
                    ACL='public-read')
