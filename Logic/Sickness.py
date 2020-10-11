import collections


class Sickness:
    def __init__(self, name):
        self.name = name
        self.queue_for_doctor = collections.deque([])
        self.is_doctor_available = True

    def add_patient_to_queue(self, new_patient):
        self.queue_for_doctor.appendleft(new_patient)

    def remove_patient_from_queue(self):
        return self.queue_for_doctor.pop()


