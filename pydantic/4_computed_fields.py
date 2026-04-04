from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float #kg
    height: float #mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi

def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print("BMI", patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print("inserted")
    
patient_info = {
    'name': 'tanishq',
    'email': 'abc@hdfc.com', # used field validator here
    'age': 70,
    'weight': 75.2,
    'height': 1.72,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '12412412412',
        'emergency': '088341348'
    }
    }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)