#===== THE GOAL ========
#To create the event model for the api-database conversion
from sqlalchemy_object import db

#Event model for Calendar Events in database
class Event(db.Model):
            __tablename__ = 'calendar_data'
            clarity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
            title = db.Column(db.String(255), nullable=False)
            start_time = db.Column(db.DateTime, nullable=False)
            end_time = db.Column(db.DateTime, nullable=False)
            description = db.Column(db.String(255), nullable=True)
            google_soon = db.Column(db.String(225), nullable=True)
            loughborough_soon= db.Column(db.String(225), nullable=True)

class Sleep_Entry(db.Model):
            __tablename__ = 'sleep_data'
            date = db.Column(db.Date ,primary_key=True, nullable=False)
            wake_up = db.Column(db.BigInteger ,nullable=True)
            fall_asleep = db.Column(db.BigInteger ,nullable=True)

