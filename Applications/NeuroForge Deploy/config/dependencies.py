import os

NEUROFORGE_SDK_VERSION = '1.0.0'

NEUROFORGE_DEPLOY_PLATFORMS = [
    'aws',
    'gcp',
    'azure',
]

# Set environment variable for NeuroForge SDK
os.environ['NEUROFORGE_SDK_VERSION'] = NEUROFORGE_SDK_VERSION
