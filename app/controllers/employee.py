import json
from flask.views import MethodView
from flask import jsonify, request
from app.db.postgresql.model import User
from app.db.postgresql.psql_manager import PSQLManager
from app.helpers.error_handler import PSQLError
from app.helpers.user_func import UserFunc

psql_tool = PSQLManager()
psqle = PSQLError()
user_util = UserFunc()

class Employee(MethodView):

    def get(self):
        try:
            id_u = request.headers.get("idUser")
            data_user = psql_tool.get_by_id(User, id_u)
            msg = psqle.msg(data_user)
            if msg.get('status') != 'ok':
                return jsonify(msg), 400
            return jsonify({'data': data_user.as_dict_format()}), 200
        except Exception as ex:
            return jsonify({'status': 'get_exception_controller', 'ex': str(ex)}), 400

    def post(self):
        try:
            employee = request.get_json()
            new_user = user_util.create_user(User, employee)
            state = psql_tool.add(new_user)
            msg = psqle.msg(state)
            if msg.get('status') == 'ok':
                return jsonify({'status': 'ok', 'id_user': str(new_user.id_user)}), 200
            else:
                return jsonify(msg), 400            
        except Exception as ex:
            return jsonify({'status': 'post_exception_controller', 'ex': str(ex)}), 403

    def put(self):
        employee = request.get_json()
        id_u = request.headers.get("idUser")
        employee_data = psql_tool.get_by_id(User, id_u)
        msg = psqle.msg(employee_data)
        if msg.get('status') != 'ok':
            return jsonify(msg), 400
        user_util.update_user(employee_data, employee)
        state = psql_tool.update()
        msg = psqle.msg(state)
        if msg.get('status') != 'ok':
            return jsonify(msg), 400
        else:
            return jsonify({'status': 'ok'}), 200
