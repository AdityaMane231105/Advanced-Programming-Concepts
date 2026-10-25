from patient import management as pm
from doctor import management as dm
from billing import bill
from records import medical

patient = pm.patient_info()
doctor = dm.doctor_info()
print("Patient:", patient)
print("Doctor:", doctor)
print(bill.generate_bill(patient,2000))
print(medical.record(patient))
