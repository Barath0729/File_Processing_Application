import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Products')

def lambda_handler(event, context):
    print(json.dumps(event, indent=2))  # Debugging

    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_name = event['Records'][0]['s3']['object']['key']

        # Fetch the object from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        data = response['Body'].read().decode('utf-8')
        print(data)

        products = data.split('\n')
        for product in products:
            call(product)

        return "Products processed successfully."

    except KeyError as e:
        return f"KeyError: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def call(product):
    data = product.split(',')
    if len(data) >= 3:
        # Insert the product data into DynamoDB
        table.put_item(Item={
            'id': data[0],
            'name': data[1],
            'desc': data[2]
        })
    else:
        print(f"Invalid product data: {product}")
