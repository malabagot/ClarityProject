#======= THE GOAL ===========
# To get api outputs and store it into the database.
from event_models import Event
from sqlalchemy_object import db
import datetime

#Stores events into the database(Imported from calendar_service)
def event_storer(events_result):
    for event in events_result:
        print("here is what the event looks like:",event)
        new_event = Event(
            title = event['summary'],
            start_time = datetime.datetime.fromisoformat(event['start']['dateTime']),
            end_time = datetime.datetime.fromisoformat(event['end']['dateTime']),
            description = event['description'],
            google_soon = event['id']
            )
        print("Api event converted ito python object=========================================")
        db.session.add(new_event) 
        print("SQLAlchemy puts python object into database===================================")
    db.session.commit()
    print("Python Objects saved to database==================================================")