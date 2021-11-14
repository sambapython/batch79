from threading import Thread
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


def create_vm_azure(data):
	print("creating vm in Azure.")
	time.sleep(11)
	print("done..")

data = {"os":"RHEL 8","RAM":"4GB", "cpu_cores":4,"HDD":"100GB"}
t1 = time.time()
thr_amazon = Thread(target=create_vm_amazon, args=(data,))
thr_google = Thread(target=create_vm_google, args=(data,))
thr_azure = Thread(target=create_vm_azure, args=(data,))
thr_amazon.start()
thr_google.start()
thr_azure.start()
while True:
	print("checking all threads closed?")
	check = [thr_amazon.is_alive(), thr_azure.is_alive(),thr_google.is_alive()]
	print(check)
	if any(check):
		time.sleep(1)
	else:
		break

print(time.time()-t1)