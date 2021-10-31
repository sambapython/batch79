from models import database
class Department:
    table_name = "department"
    def __init__(self, dept_id, dept_name):
        self.name = dept_name 
        self.id=dept_id

    @classmethod
    def create_table(cls):
        query=f"create table if not exists {cls.table_name} (id int not null, name varchar(250), primary key(id))"
        database.execute_query(query)

    def insert(self):
        query = f"insert into {self.table_name}(id,name) values({self.id},'{self.name}')"
        database.execute_query(query)

Department.create_table()