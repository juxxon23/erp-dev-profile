from .controllers.employee import Employee
from .controllers.all_employee import AllEmployee

user = {
    "employee": "/employee", "view_func_employee": Employee.as_view("app_employee"),
    "allemployee": "/allemployee", "view_func_allemployee": AllEmployee.as_view("app_allemployee")
}
