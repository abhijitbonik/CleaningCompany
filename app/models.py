from app import db


class Worker(db.Document):
    email = db.EmailField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    dob = db.StringField()
    identification=db.StringField()
    phone = db.IntField()
    availibility = db.BooleanField()

class Equipment(db.Document):
    uid=db.StringField()
    etype=db.StringField()
    brand=db.StringField()
    model=db.StringField()
    remarks=db.StringField()
    availibility=db.BooleanField()

class Vehicle(db.Document):
    name=db.StringField()
    seats=db.IntField()
    uid=db.StringField()
    availibility=db.BooleanField()

class Address(db.EmbeddedDocument):
    addressLine1=db.StringField()
    addressLine2=db.StringField()
    landmark=db.StringField()
    zipcode=db.StringField()
    city=db.StringField()
    state=db.StringField()

class Jobs(db.Document):
    customer_name=db.StringField()
    job_address=db.EmbeddedDocumentField(Address)
    billing_address=db.EmbeddedDocumentField(Address)
    email=db.EmailField()
    customer_phone=db.IntField()
    description=db.StringField()
    size=db.StringField()
    expectedStartDate=db.DateTimeField()
    expectedEndDate=db.DateTimeField()
    costPerWorker=db.FloatField()
    assignedWorkers=db.ListField(db.ReferenceField(Worker))
    costPerVehicle=db.FloatField()
    assignedVehicles=db.ListField(db.ReferenceField(Vehicle))
    cleaningEquipments=db.ListField(db.ReferenceField(Equipment))
    status=db.BooleanField()

class AssignJob(db.Document):
    worker=db.ReferenceField(Worker)
    job=db.ReferenceField(Jobs)
    assign_from=db.DateTimeField()
    assign_till=db.DateTimeField()
    status=db.BooleanField()

