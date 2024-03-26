import os

# Create a deployment directory
deployment_dir = 'deployment'
os.makedirs(deployment_dir, exist_ok=True)

# Copy the saved model to the deployment directory
shutil.copy('model.pt', deployment_dir)

# Add necessary files and directories to deployment directory
# e.g. copy any necessary datasets, pip requirements, scripts, etc.

# Create a requirements.txt file
with open(os.path.join(deployment_dir, 'requirements.txt'), 'w') as f:
    f.write('torch')

# Create a deployment package
with zipfile.ZipFile(os.path.join(deployment_dir, 'deployment.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(deployment_dir):
        for file in files:
            z.write(os.path.join(root, file))
