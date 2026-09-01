from event_models import Sleep_Entry
from sqlalchemy_object import db
import datetime

def sleep_storer(sleep_object):
    new_sleep_object = Sleep_Entry(
        date = str(datetime.datetime.today()).split()[0],
        wake_up =  int(int(sleep_object["wakeup_hh"])*3600 + int(sleep_object["wakeup_mm"])*60 + datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp()),
        fall_asleep =  int(int(sleep_object["fallasleep_hh"])*3600 + int(sleep_object["fallasleep_mm"])*60 + datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp()),
        )
    db.session.add(new_sleep_object)
    db.session.commit()

