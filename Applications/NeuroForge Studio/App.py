import os
from clarifai.client import ClarifaiApp

# Set up Clarifai app
APP = ClarifaiApp(api_key=os.environ['CLARIFAI_API_KEY'])

def list_apps():
    """List all the apps available in the user's account."""
    apps = APP.users.list_apps()
    for app in apps:
        print("App id: ", app.id)

def upload_input(app_id, image_url, labels):
    """Upload an input to a specific app."""
    INPUTS = APP.inputs.new_inputs_from_url(
        user_id="your_user_id", app_id=app_id,
        inputs=[
            {
                'data': {'image': {'url': image_url}},
                'concepts': [[{'name': label, 'value': 0.9} for label in labels]]
            }
        ]
    )
    print("Inputs Uploaded")

def delete_app(app_id):
    """Delete an app."""
    user = APP.users.get_current_user()
    deleted_app = user.apps.delete_app(app_id)
    print("App deleted")

# List all the apps
list_apps()

# Upload an input to an app
app_id = "test_app_id"
image_url = "https://example.com/image.jpg"
labels = ["red", "car"]
upload_input(app_id, image_url, labels)

# Delete an app
app_id = "test_app_id_to_delete"
delete_app(app_id)
