from app import add, call_api, get_users
import app
from unittest.mock import patch
# res=add(10,20)
# if res==30:
# 	print("scuccess")
# else:
# 	print("failed")

class MOCKED_RESP:
	def __init__(self):
		self.status_code=200

	def json(self):
		return {"data":[{"fname":"sfdsf"}]}

import unittest
class TestCallAPI(unittest.TestCase):

	@patch('app.call_api')
	def test_call_api(self, mock_call_api):
		mock_call_api.return_value=MOCKED_RESP()
		self.assertIsNotNone(get_users())





class TestApp(unittest.TestCase):

	def parse_response(self):
		print("this is parsere")

	@classmethod
	def setUpClass(cls):
		print("this is setup") 
		print("login")
		cls.token="user1"

	@classmethod
	def tearDownClass(cls):
		print("this is logout")
		cls.token=""

	def setUp(self):
		print("PREPARE THE TEST DATA")
	def tearDown(self):
		print("REMOVE THE TEST DATA")


	def test_add_10_20(self):
		print("executing test_add_10_20 with token:%s"%self.token)
		expected=30
		actual= add(10,20)
		self.assertEqual(expected, actual, "test_add_10_20 failed.")

	def test_add_12_23(self):
		print("executing test_add_12_23 with token:%s"%self.token)

		expected=3.5
		actual= add(1.2,2.3)
		self.assertTrue(expected==actual, "test_add_12_23 failed.")

	def test_add_str1_10(self):
		print("executing test_add_str1_10 with token:%s"%self.token)

		# expected = None 
		# actual = add("str1",10)
		self.assertIsNone(add("str1",10), "test_add_str1_10")



# testapp = TestApp()
# testapp.test_add_10_20()
unittest.main()