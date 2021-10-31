import psycopg2
import constants
def get_conn():
    dns = f"dbname={constants.DB_NAME} user={constants.USER} password={constants.PASSWORD}"
    con = psycopg2.connect(dns)
    cur = con.cursor()
    return con, cur

def execute_query(query):
    con,cur = get_conn()
    cur.execute(query)
    con.commit()
    con.close()

