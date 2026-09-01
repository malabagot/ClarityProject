#========== THE GOAL ===========
# Get the events from external calendars such as moodle and google calendar via their api's.

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from app import app
from calendar_database_handler import event_storer

#This says we can only read from the calendar, no writing
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def main():
    with app.app_context():
    
        #Sets the credentials to None for accessing the api
        creds = None



        #If the token file already exist on the pc then take the credentials from it  
        if os.path.exists("token.json"):  
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        else:
            #if theres no credentals or the credentials arent valid
            if not creds or not creds.valid:
                #check if the credentials are expired and can be refreshed (By checking if the secret refresh token is still valid)
                if creds and creds.expired and creds.refresh_token:
                    print("Refreshing token")
                    creds.refresh(Request())
                #if not, open the browser Oauth consent screen to get a new manually authroised token
                else:
                    print("Getting fresh token")
                    flow = InstalledAppFlow.from_client_secrets_file(
                        "credentials.json", SCOPES
                    )
                    creds = flow.run_local_server(port=8080)
                    

                #open the file called token.json and write to it the credentials in json format.
                with open("token.json", "w") as token:
                    token.write(creds.to_json())

        #We try because there may be an error, we want to catch that error for debugging purposes if it apepars
        try:
            #actually connect to google by connecting to the calendar called "calendar" with v3 of the api and the respective credentials
            service = build("calendar", "v3", credentials=creds)

            # Call the Calendar API
            now = datetime.datetime.now(tz=datetime.timezone.utc) # datetime is the module name, but datetime is the also the name of the class we take from it
            next_week = (now + datetime.timedelta(days=7)).isoformat() # we pre-calculate the isoformat datetime for what a week away from now would be

            print("Getting the upcoming 10 events")
            api_result = (
                service.events() #Initiate the events part of the google api connection
                .list( #This is the method that says list out all of the events that bla bla bla
                    calendarId="primary",
                    timeMin=now.isoformat(),
                    timeMax=next_week,
                    maxResults=10,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute() # this actually sends the request to the google api
                    )

            events_result = api_result['items']
            if events_result:
                print("Non empty event dictionary recieved")
                event_storer(events_result)
            else:
                print("Theres no events in the next week=================================================")

                            

        except HttpError as error:
            print(f"An error occurred: {error}")


if __name__ == "__main__": #__name__ is a python variable that says why this file was run
    main()                   # if the file was run by itself, it will be __main__, it it was run by another file, it wouldnt be