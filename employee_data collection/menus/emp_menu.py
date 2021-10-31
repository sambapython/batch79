from models.emp import Employee
def insert_menu():
	emp_id = input("Enter employee ID:")
	emp_name = input("Enter employee Name:")
	emp_salary = input("Enter employee Salary:")
	emp_instance = Employee(emp_name, emp_id, emp_salary)
	emp_instance.insert()
	print("Employee saved successfully")

def update_menu():
	pass 

def delete_menu():
	pass