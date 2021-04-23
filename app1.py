import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('jim1.jpg','Jim'),
      ('jim2.jpg','Jim'),
      ('jim3.jpg','Jim'),
      ('tim1.jpg','Tim'),
      ('tim2.jpg','Tim'),
      ('tim3.jpg','Tim')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('ecb3ac-cs4740-pa5','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )
