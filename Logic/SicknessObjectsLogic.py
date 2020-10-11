from Logic import Sickness
from UI import MainMenu

sickness_list = []


def initializer():
    sickness_list.append(Sickness.Sickness("Flue"))
    sickness_list.append(Sickness.Sickness("Coronavirus"))
    sickness_list.append(Sickness.Sickness("Herpes"))
    sickness_list.append(Sickness.Sickness("Rabies"))
    MainMenu.main_menu_screen()


def queue_handler(new_patient):
    if new_patient.sickness.is_doctor_available:
        new_patient.sickness.is_doctor_available = False
        new_patient.change_patient_status_to_is_currently_with_doctor()
    else:
        new_patient.sickness.add_patient_to_queue(new_patient)


def free_doctor(sickness):
    sickness.is_doctor_available = True
    next_patient = sickness.remove_patient_from_queue()
    queue_handler(next_patient)
