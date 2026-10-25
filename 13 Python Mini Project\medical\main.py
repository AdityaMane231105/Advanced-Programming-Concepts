from Patient.patient import patient_info
from Doctor.doctor import doctor_info
from Billing.billing import bill
from Records.records import medical_record
 
print(patient_info())
print(doctor_info())
print("Bill:", bill())
print(medical_record())
