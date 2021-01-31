#class Class:
#    def __init__(self, room_number: str, course_id: str, time: int):
#        self.room = room_number
#        self.number = course_id
#        self.time = time
class Klass:
    pass

def Class_constructor(room_number: str, course_id: str, time: int):
    c = Klass()
    c.room = room_number
    c.number = course_id
    c.time = time
    return c
print(Class_constructor("OH321", "MC27", 1230).time)
