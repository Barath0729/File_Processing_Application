import json
import boto3

s3_client = boto3.client('s3')
lambda_client = boto3.client('lambda')

def lambda_handler(event, context):
    print(json.dumps(event, indent=2))  # Log the incoming event

    # Check if the expected structure exists in the event
    if 'Records' in event and len(event['Records']) > 0:
        try:
            # Extract bucket and file name from the event
            bucket_name = event['Records'][0]['s3']['bucket']['name']
            file_name = event['Records'][0]['s3']['object']['key']

            if file_name == 'products.csv':
                # Prepare the payload to send to Lambda 2
                payload = {
                    'Records': event['Records']
                }
                lambda_client.invoke(
                    FunctionName='file_processing_worker',  # Replace with actual name of Lambda 2
                    InvocationType='Event',  # Asynchronous invocation
                    Payload=json.dumps(payload)
                )
                return "Routing to 2nd Lambda"
            else:
                raise ValueError(f"File {file_name} not processed, only 'products.csv' is allowed.")

        except KeyError as e:
            return f"KeyError: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        print("Event structure is invalid. Here's the event:")
        print(json.dumps(event, indent=2))
        return "Invalid event structure"
import json
import boto3

s3_client = boto3.client('s3')
lambda_client = boto3.client('lambda')

def lambda_handler(event, context):
    print(json.dumps(event, indent=2))  # Log the incoming event

    # Check if the expected structure exists in the event
    if 'Records' in event and len(event['Records']) > 0:
        try:
            # Extract bucket and file name from the event
            bucket_name = event['Records'][0]['s3']['bucket']['name']
            file_name = event['Records'][0]['s3']['object']['key']

            if file_name == 'products.csv':
                # Prepare the payload to send to Lambda 2
                payload = {
                    'Records': event['Records']
                }
                lambda_client.invoke(
                    FunctionName='file_processing_worker',  # Replace with actual name of Lambda 2
                    InvocationType='Event',  # Asynchronous invocation
                    Payload=json.dumps(payload)
                )
                return "Routing to 2nd Lambda"
            else:
                raise ValueError(f"File {file_name} not processed, only 'products.csv' is allowed.")

        except KeyError as e:
            print(f"KeyError occurred: {str(e)}")
            raise  # Re-raise the exception to let Lambda handle the failure
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            raise  # Re-raise the exception to let Lambda handle the failure
    else:
        print("Event structure is invalid. Here's the event:")
        print(json.dumps(event, indent=2))
        raise ValueError("Invalid event structure")
