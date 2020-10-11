import collections

flue_patients_queue = collections.deque([])
coronavirus_patients_queue = collections.deque([])
herpes_patients_queue = collections.deque([])
rabies_patients_queue = collections.deque([])
doctors_availability = {
    "Flue": True,
    "Coronavirus": True,
    "Herpes": True,
    "Rabies": True
}


def add_patient_to_queue(new_patient, sickness):
    #patients_queue.appendleft(new_patient)
    pass

def remove_patient_from_queue():
    #patients_queue.pop()
    pass


def is_doctor_available(sickness):
    #return doctors_availability.get(sickness)
    pass
