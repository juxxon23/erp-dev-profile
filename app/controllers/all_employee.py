import json
from flask.views import MethodView
from flask import jsonify, request
from app.db.postgresql.model import User
from app.db.postgresql.psql_manager import PSQLManager
from app.helpers.error_handler import PSQLError

psql_tool = PSQLManager()
psqle = PSQLError()

class AllEmployee(MethodView):

    def get(self):
        try:
            all_employees = psql_tool.get_all(User)
            msg = psqle.msg(all_employees)
            if msg.get('status') != 'ok':
                return jsonify(msg), 400
            employee_list = []
            for employee in all_employees:
                employee_list.append(employee.as_dict())
            return jsonify({"status":"ok", "employee_list":employee_list}), 200
        except Exception as ex:
            return jsonify({'status': 'get_exception_controller', 'ex': str(ex)}), 400