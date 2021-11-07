# import time
# print("started")
# try:
#     print(1/0)
#     time.sleep(10)
#     print("try")
# except Exception as err:
#     print("Exception as err executed")
#     print(err)
# except:
#     print("except executed")
# print("main block executed")
# write some data in to file while it is writing restart machine and whether except block executing or not.

print("started")
try:
    f=open("data.txt","w")
    for in in range(10000):
        f.write("some data%s\n"%i)
        time.sleep(1)
    print("try")
except Exception as err:
    print("Exception as err executed")
    print(err)
except:
    f.close()
    print("except executed")
print("main block executed") 