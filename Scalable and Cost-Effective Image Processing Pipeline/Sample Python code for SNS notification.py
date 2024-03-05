#If using SNS notifications, create an SNS topic.
#Grant Lambda function permissions to publish to the topic.
#Sample Python code for SNS notification:

import boto3

def send_sns_notification(message):
    sns_client = boto3.client('sns')
    sns_arn = 'your-sns-topic-arn'  # Replace with your SNS topic ARN
    sns_client.publish(TopicArn=sns_arn, Message=message)
