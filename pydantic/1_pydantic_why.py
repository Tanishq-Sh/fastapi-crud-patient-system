from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of the patient in less than 50 chats", examples=["Tanishq", "Mahati"])]
    # email: EmailStr
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="Is the patient married or not")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_digits=5)]
    contact_details: Dict[str, str]
    
    
def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("inserted")
    
patient_info = {
    'name': 'tanishq',
    'email': 'abc@gmail.com',
    'linkedin_url': 'http://linkedin.com/12414',
    'age': '20',
    # 'weight': 75.2,
    'weight': '75.2', # works for strict=False
    # 'married': True,
    # 'allergies': ['pollen', 'dust'],
    'contact_details': {
        'email': 'abc@gmail.com',
        'phone': '12412412412'
    }
    }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)