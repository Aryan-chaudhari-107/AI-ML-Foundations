#--> uvicorn main:app –reload <-- (command to run file)

from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json


# Utility Fucntion
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)


#Created app
app = FastAPI()


# Model created for data validation (pydantic concept)
# For Create new Patient Model
class Patient(BaseModel):
    id: Annotated[str, Field(..., description='Id of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., decription='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male','female','others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(...,gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(...,gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self)  -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi 
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'UnderWeight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obses'


#For update Patient Model
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None)]
    gender: Annotated[Optional[Literal['male','female','others']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]



#------------------
# GET:
#------------------

#1st end point:
@app.get("/home")
def hello():
    return {'message': 'patient Management System API'}


#2nd end point:
@app.get("/about")
def about():
    return {'message': 'A fully functional API to manage your patient records'}


#3rd end point:
@app.get("/view")
def view():
    data = load_data()
    return data


#4th end point: (using path function)
@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path(..., description= 'Id of the patient in the DB', examples='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code =404, detail="Patient not found")


#5th end point: (using Query fucntion)
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order == 'desc' else False
    sorted_data =  sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse = sort_order)
    
    return sorted_data



#------------------
# POST:
#------------------

@app.post('/create')
def create_patient(patient:Patient):

    # load existing data
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException (status_code=400, detail='Patient is already exists')
    

    # if new patient add to the database
    # --> Existing data is a Python dictionary
    # --> Data we receive is JSON
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into json file
    save_data(data)

    return JSONResponse(status_code=200, content={'messge':'Patienft created successfully'})



#------------------
# PUT:
#------------------

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    
    #load data
    data = load_data()

    #check if the patient already exists
    if patient_id not in data:
        raise HTTPException(status_code=400, detail='Patient not found')
    
    #Fetch patinet info (dict)
    existing_patient_info = data[patient_id]


    # --> Existing data is a Python dictionary
    # --> Data we receive is JSON
    updated_patient_info = patient_update.model_dump(exclude_unset=True)


    # merge old + new data
    updated_patient_info = {**existing_patient_info, **updated_patient_info}


    # add id temporarily for validation
    updated_patient_info['id'] = patient_id

    
    # dict --> pydantic object
    Patient_pydantic_obj = Patient(**updated_patient_info)


    # pydantic object --> dict
    updated_patient_info = Patient_pydantic_obj.model_dump(exclude='id')


    # update database
    data[patient_id] = updated_patient_info
    
    # save data
    save_data(data)

    return JSONResponse(status_code=200, 
                        content={
                            'message': 'Patient updated successfully',
                            'updated_patient' : updated_patient_info }
                        )



#------------------
# DELETE:
#------------------

@app.delete('/delete/{patient_id}')

def delete_patient(patient_id: str):

     #load data
    data = load_data()

    #check if the patient already exists
    if patient_id not in data:
        raise HTTPException(status_code=400, detail='Patient not found')

    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'Patient deleted'})
