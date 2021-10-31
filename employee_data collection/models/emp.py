from models import database
class Employee:
    table_name="emp"
    def __init__(self,emp_name,emp_id,emp_sal):
        self.name=emp_name
        self.id=emp_id
        self.salary=emp_sal

    def get(self):# instance method
        print(f"Employee Name:{self.name}, id:{self.id}, salary:{self.salary}")

    def insert(self):
        query = f"insert into {self.table_name}(id,name,salary) values({self.id},'{self.name}',{self.salary})"
        database.execute_query(query)

    @classmethod
    def create_table(cls):
        query=f"create table if not exists {cls.table_name} (id int not null, name varchar(250), salary int, primary key(id))"
        database.execute_query(query)
Employee.create_table()