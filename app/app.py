from flask import Flask, render_template
from faker import Faker
from load_balancer import LoadBalancer
from services.patient_service.patient_service import PatientService
from services.vital_signs_service.vital_signs_service import VitalSignsService
from services.consultation_service.consultation_service import ConsultationService
from services.doctor_service.doctor_service import DoctorService

app = Flask(__name__)
load_balancer = LoadBalancer([PatientService(), VitalSignsService(), ConsultationService(), DoctorService()])

@app.route('/')
def index():
    fake = Faker()
    patients = [fake.name() for _ in range(5)]  # Generate a list of 5 patient names
    vital_signs = ["Blood Pressure: 120/80", "Glucose Level: 90 mg/dL"]  # Sample vital signs data
    consultations = ["General check-up", "Follow-up appointment"]  # Sample consultation data
    doctors = ["Dr. Smith", "Dr. Johnson"]  # Sample doctor data
    return render_template('index.html', patients=patients, vital_signs=vital_signs, consultations=consultations, doctors=doctors)

if __name__ == '__main__':
    app.run()
