import requests

def call_api(url):
	return requests.get(url)

def get_users():
	url = "https://reqres.in/api/users?page=2"
	resp = call_api(url)
	data = resp.json()
	return data.get("data")







def add(x,y):
	"""
	add(10,20)
	add(10.34,24.56)
	"""
	print("fdafas")
	try:
		return x+y 
	except Exception as err:
		#print(result)
		print(err)


# print(add(10,20))
# print(add(1.2,3.4))