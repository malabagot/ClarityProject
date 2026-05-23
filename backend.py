import requests
import json


class Example:
    def __init__(self, test):
        self.test_value = test

example = Example("erwerwerwe")
print(example.test_value)
exit()















session = requests.Session()

# Login to lboro
req = session.post("https://my.lboro.ac.uk/campusm/sso/ldap/2548",data={
    "username": "yb0112",
    "password": "200%guyanese25GTR"
})

# Fetch timetable
req = session.get("https://my.lboro.ac.uk/campusm/sso/cal2/course_timetable?start=2025-11-01T00%3A00%3A00.000Z&end=2025-12-31T23%3A59%3A59.000Z")
data = json.loads(req.text)
for event in data["events"]:
    print(event.get("teacherName", "No teacher."))


# class LboroCalendar:
    
# def main():
    