from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'User'

    id_user = db.Column(db.String(10), primary_key=True, nullable=False, unique=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)  
    phone_number = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    employee_id = db.Column(db.String(10), nullable=False)
    dateof_hire = db.Column(db.DateTime, nullable=False)
    job_title = db.Column(db.String(30), nullable=False)
    
    def __init__(self, id_user, first_name, last_name, email, phone_number, address, employee_id, dateof_hire, job_title):
        self.id_user = id_user
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.employee_id = employee_id
        self.dateof_hire = dateof_hire
        self.job_title = job_title
