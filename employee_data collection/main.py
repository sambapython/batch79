from menus import dept_menu, emp_menu
print("Operations:")
print("1. Employee\n2.Department")
opt = input("Enter an option:")
if opt == "1":
	print("Employee Operations")
	print("1.Insert\n2.update\n3.delete")
	opt = input("Enter na option:")
	if opt == "1":
		emp_menu.insert_menu()
	elif opt == "2":
		menus.update_menu()
	elif opt == "3":
		menus.delete_menu()
	else:
		print("Wrong option")

elif opt == "2":
	print("Department Oprtations")
	print("1.Insert\n2.update\n3.delete")
	opt = input("Enter na option:")
	if opt == "1":
		dept_menu.insert_menu()
	elif opt == "2":
		menus.update_menu()
	elif opt == "3":
		menus.delete_menu()
	else:
		print("Wrong option")

