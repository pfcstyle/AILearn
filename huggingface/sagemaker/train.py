import sagemaker
import boto3

try:
    role = sagemaker.get_execution_role()
except ValueError:
    iam_client = boto3.client('iam')
    role = iam_client.get_role(RoleName='AmazonSageMaker-ExecutionRole-20230912T165556')['Role']['Arn']
sess = sagemaker.Session()