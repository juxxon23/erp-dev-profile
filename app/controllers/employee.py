import secrets
import json
from flask.views import MethodView
from flask import jsonify, request
from app.db.postgresql.model import User
from app.db.postgresql.psql_manager import PSQLManager
from app.helpers.error_handler import PSQLError

psql_tool = PSQLManager()
psqle = PSQLError()


class Employee(MethodView):

    def get(self):
        try:
            all_employees = psql_tool.get_all(User)
            msg = psqle.msg(employee_list)
            if msg.get('status') != 'ok':
                return jsonify(msg), 400
            employee_list = []
            for employee in all_employee:
                temp_employee = {
                    "idUser":employee.id_user,
                    "firstName":employee.first_name,
                    "lastName":employee.last_name,
                    "email":employee.email,
                    "phoneNumber":employee.phone_number,
                    "address":employee.address,
                    "personalID":employee.employee_id,
                    "dateofHire":employee.dateof_hire,
                    "jobTitle":employee.job_title
                }
                employee_list.append(temp_employee)
            return jsonify({"status":"ok", "employee_list":employee_list}), 200
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)}), 403

    def post(self):
        try:
            employee = request.get_json()
            new_user = User(
                id_user=secrets.token_hex(5),
                first_name=employee['firstName'],
                last_name=employee['lastName'],
                email=employee['email'],
                phone_number=employee['phoneNumber'],
                address=employee['address'],
                employee_id=employee['employeeID'],
                dateof_hire=employee['dateofHire'],
                job_title=employee['jobTitle']
                )
            state = psql_tool.add(new_user)
            msg = psqle.msg(state)
            if msg.get('status') == 'ok':
                return jsonify({'status': 'ok', 'id_user': str(new_user.id_user)}), 200
            else:
                return jsonify(msg), 400            
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)}), 403
