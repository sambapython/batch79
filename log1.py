import logging
logging.basicConfig(level=logging.DEBUG, filename="log.txt",
    format="%(asctime)s==>%(levelname)s=>%(message)s")# asctime, levelname,message
logging.info("start")
class RolebaseAccessError(Exception):
    pass
    
a=input("enter a value:")
b=input("enter b value:")
logging.debug(f"befor conversion a={a}, b={b}")
try:
    a=float(a)
    b=float(b)
    if b==12:
        raise RolebaseAccessError("No access for b value 12")
    logging.debug(f"after conversion a={a}, b={b}")
    res=a/b
    print(f"result={res}")
except ZeroDivisionError as err:
    logging.error("not expected b value 0")
    
except ValueError as err:
    logging.error("expecting only numbers..")
    
except RolebaseAccessError as err:
    logging.error("Don't have an access to work with b=12")
    
except Exception as err:
    logging.error(str(err))
logging.info("end")