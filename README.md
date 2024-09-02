###AWS Lambda-based File Processing with S3 and SNS Integration

Key Components:
1.AWS S3
2.AWS Lambda
3.AWS SNS
4.AWS IAM
5.AWS CloudWatch Logs

![Retrospectives](https://github.com/user-attachments/assets/b3196854-5872-47f6-bea4-5e7e47aeb2c5)


###Flow of Operations:
File Upload: A file is uploaded to an S3 bucket.
S3 Event Trigger: S3 generates an event, which triggers the first Lambda function.
File Validation:
The Lambda function checks if the uploaded file is named products.csv.
If the file is valid, the function invokes the second Lambda for processing.
If the file name is incorrect, an error is raised, and a failure notification is sent via SNS.
File Processing: The second Lambda function processes the file content if the validation succeeds.
Error Handling:
If an error occurs during file validation, Lambda raises an exception, which is captured by AWS Lambda Destinations, and SNS sends an alert.

![Screenshot (129)](https://github.com/user-attachments/assets/087ae6ee-962e-4155-9ba6-54842a5ef897)


###Benefits:
Cost Efficiency: By using a serverless architecture (AWS Lambda), costs are minimized since the system only runs when triggered by an event.
Scalability: The system automatically scales based on the number of incoming file uploads.
Real-Time Alerts: SNS ensures that any failures are immediately reported, enabling quicker responses to issues.
Seamless Integration: Different AWS services are integrated to form a cohesive and reliable file processing pipeline.
