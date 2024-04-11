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
            employee_list = psql_tool.get_all(User)
            msg = psqle.msg(employee_list)
            if msg.get('status') != 'ok':
                return jsonify(msg), 400
            el = []
            for e in employee_list:
                e = {
                    "id_user":e.id_user,
                    "first_name":e.first_name,
                    "last_name":e.last_name,
                    "email":e.email,
                    "phone_number":e.phone_number,
                    "address":e.address,
                    "employee_id":e.employee_id,
                    "dateof_hire":e.dateof_hire,
                    "job_title":e.job_title
                }
                el.append(e)
            return jsonify({"status":"ok", "employee_list":el}), 200
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)}), 403

    def post(self):
        try:
            employee = request.get_json()
            new_user = User(
                id_user=secrets.token_hex(5),
                first_name=employee['first_name'],
                last_name=employee['last_name'],
                email=employee['email'],
                phone_number=employee['phone_number'],
                address=employee['address'],
                employee_id=employee['employee_id'],
                dateof_hire=employee['dateof_hire'],
                job_title=employee['job_title']
                )
            state = psql_tool.add(new_user)
            msg = psqle.msg(state)
            if msg.get('status') == 'ok':
                return jsonify({'status': 'ok', 'id_user': str(new_user.id_user)}), 200
            else:
                return jsonify(msg), 400            
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)}), 403
