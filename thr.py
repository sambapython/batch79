import time
def create_vm_amazon(data):
	# it has to connect with amazona cloud, and create vm.
	print("creating vm in amazon.")
	time.sleep(10)
	print("done..")

def create_vm_google(data):
	print("creating vm in google.")
	time.sleep(8)
	print("done..")


def create_vm_azure():
	print("creating vm in Azure.")
	time.sleep(11)
	print("done..")

data = {"os":"RHEL 8","RAM":"4GB", "cpu_cores":4,"HDD":"100GB"}
t1 = time.time()
create_vm_amazon(data)
create_vm_google(data)
create_vm_azure(data)
print(time.time()-t1)