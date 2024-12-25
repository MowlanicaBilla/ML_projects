import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scope and API version
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
API_VERSION = 'v1'

def get_credentials():
    creds = None

    # The file token.json stores the user's access and refresh tokens, and it is
    # created automatically when the authorization flow completes for the first time.
    token_path = 'token.json'
    credentials_path = 'credentials.json'

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return creds

def list_messages(service, user_id='me', query=''):
    try:
        response = service.users().messages().list(userId=user_id, q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, q=query, pageToken=page_token).execute()
            messages.extend(response['messages'])

        return messages

    except Exception as error:
        print(f'An error occurred: {error}')
        return None

def delete_messages(service, user_id='me', message_ids=[]):
    try:
        for message_id in message_ids:
            service.users().messages().delete(userId=user_id, id=message_id['id']).execute()
            print(f"Deleted message {message_id['id']}")
    except Exception as error:
        print(f'An error occurred: {error}')

def main():
    creds = get_credentials()
    service = build('gmail', API_VERSION, credentials=creds)

    # Example: List all messages with a specific label
    label_name = 'INBOX'  # Change this to the label you want to process
    query = f'label:{label_name}'
    messages = list_messages(service, query=query)

    if messages:
        print(f"Total messages in '{label_name}': {len(messages)}")

        # Count messages from each sender
        sender_counts = {}
        for message in messages:
            headers = service.users().messages().get(userId='me', id=message['id'], format='metadata').execute()
            sender = next((header['value'] for header in headers['payload']['headers'] if header['name'] == 'From'), None)

            if sender:
                sender_counts[sender] = sender_counts.get(sender, 0) + 1

        # Display sender counts
        print("Sender Counts:")
        for sender, count in sender_counts.items():
            print(f"{sender}: {count} emails")

        # # Example: Delete all messages from a specific sender
        # sender_to_delete = 'example@example.com'  # Change this to the sender you want to delete
        # messages_to_delete = [message for message in messages if sender_to_delete in message['payload']['headers'][17]['value']]
        # delete_messages(service, message_ids=messages_to_delete)

if __name__ == '__main__':
    main()
