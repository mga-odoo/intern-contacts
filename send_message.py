import firebase_admin
from firebase_admin import auth
from firebase_admin import messaging
from firebase_admin import credentials

# This registration token comes from the client FCM SDKs.
registration_token = 'ccf1-MwxPDA:APA91bFCmxFzOVz4C5BcoJS_WObG4OuUwUwAlBkSSfmGRtC7PBFf4PAbF5tabqe0kQzy8KSc201vJcFCZQpgQu_Am6-cl1FvdzfbVn__G9QqBSPlv7pnOCONRM_9gz1QWtYLFLzcrGsK'

cred = credentials.RefreshToken('service-account-file.json')
default_app = firebase_admin.initialize_app(cred)
# See documentation on defining a message payload.
message = messaging.Message(
    data={
        'score': '850',
        'time': '2:45',
    },
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)

