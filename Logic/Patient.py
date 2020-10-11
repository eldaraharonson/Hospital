import datetime


class Patient:
    def __init__(self, name, sickness):
        self.name = name
        self.sickness = sickness
        self.status = "Waiting"
        self.time_arrived = datetime.datetime.now().strftime("%H:%M")

    def change_patient_status_to_is_currently_with_doctor(self):
        self.status = "With doctor"


    def change_patient_status_to_finished_treatment(self):
        self.status = "Finished treatment"
        #bring new patient to doctor