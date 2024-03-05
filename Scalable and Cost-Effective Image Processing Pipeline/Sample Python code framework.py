#Author a Python (or Node.js) Lambda function to handle image processing.
#Integrate with an image processing library like Pillow (Python) or Sharp (Node.js).
#Sample Python code framework:


import boto3
from PIL import Image

def lambda_handler(event, context):
    # Get image object from S3
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        # Download image
        download_path = '/tmp/downloaded_image.jpg'  # Adjust as needed
        s3.download_file(bucket, key, download_path)

        # Process image using Pillow
        with Image.open(download_path) as image:
            resized_image = image.resize((500, 500))  # Example resizing
            resized_image.save('/tmp/resized_image.jpg')

        # Upload processed image to S3
        processed_key = 'resized/' + key  # Example path for processed images
        s3.upload_file('/tmp/resized_image.jpg', bucket, processed_key)

        # Send SNS notification (code for this later)

    except Exception as e:
        # Handle errors
        print(f"Error processing image: {e}")
