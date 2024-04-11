from .controllers.employee import Employee

user = {
    "employee": "/employee", "view_func_employee": Employee.as_view("app_employee")
}
