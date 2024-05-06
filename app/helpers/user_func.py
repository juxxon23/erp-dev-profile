import secrets
from datetime import datetime

class UserFunc:


    def create_user(self, table_name, user_data):
        return table_name(
            id_user=secrets.token_hex(5),
            first_name=user_data['firstName'],
            last_name=user_data['lastName'],
            email=user_data['email'],
            phone_number=user_data['phoneNumber'],
            address=user_data['address'],
            employee_id=user_data['personalID'],
            dateof_hire=user_data['dateofHire'],
            job_title=user_data['jobTitle']
            )

    def update_user(self, user_db, user_data):
        user_db.first_name=user_data['firstName'],
        user_db.last_name=user_data['lastName'],
        user_db.email=user_data['email'],
        user_db.phone_number=user_data['phoneNumber'],
        user_db.address=user_data['address'],
        user_db.employee_id=user_data['personalID'],
        user_db.dateof_hire=datetime.strptime(user_data['dateofHire'], '%d/%m/%Y'),
        user_db.job_title=user_data['jobTitle']