from models.dept import Department
def insert_menu():
	dept_id = input("Enter dept ID:")
	dept_name = input("Enter dept Name:")
	dept_instance = Department(dept_id, dept_name)
	dept_instance.insert()
	print("Department saved successfully")