import boto3
import io

# Create a boto3 S3 client
s3 = boto3.client('s3')

# Read the contents of the deployment package
with open(os.path.join(deployment_dir, 'deployment.zip'), 'rb') as f:
    package = f.read()

# Export the package to a cloud storage service
s3.upload_fileobj(io.BytesIO(package), 'my-neuroforge-bucket', 'deployment.zip')
