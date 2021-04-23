import boto3
import io
import PIL
from PIL import Image

rekognition = boto3.client('ecb3ac-cs4740-pa5', region_name='us-east-1')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    
image = Image.open("jim1.jpg")
stream = io.BytesIO()
image.save(stream,format="JPEG")
image_binary = stream.getvalue()


response = rekognition.search_faces_by_image(
        CollectionId='family_collection',
        Image={'Bytes':image_binary}                                       
        )
    
for match in response['FaceMatches']:
    print (match['Face']['FaceId'],match['Face']['Confidence'])
        
    face = dynamodb.get_item(
        TableName='family_collection',  
        Key={'RekognitionId': {'S': match['Face']['FaceId']}}
        )
    
    if 'Item' in face:
        print (face['Item']['FullName']['S'])
    else:
        print ('no match found in person lookup')
