from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    
    name: str
    gender: str = 'male'
    age: int
    address: Address
    # address: str # eg. - 'house no 2, sector 66, gurgaon, haryana, 122002' # complex data type, we should make another model if we want to extract info from this
    
address_dict = {
    'city': 'gurgaon',
    'state': 'haryana',
    'pin': '122001'
}

address1 = Address(**address_dict)

patient_dict = {
    'name': "Tanishq",
    'gender': 'male',
    'age': 35,
    'address': address1
}

# for checking exclude_unset
patient_dict = {
    'name': "Tanishq",
    'age': 35,
    'address': address1
}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)

temp = patient1.model_dump()
# temp = patient1.model_dump(include=['name', 'gender'])
temp = patient1.model_dump(exclude=['name', 'gender'])
temp = patient1.model_dump(exclude_unset=True) # parameters not set in patient_dict but have a default value in model won't be exported
# temp = patient1.model_dump_json()

print(temp)
print(type(temp))