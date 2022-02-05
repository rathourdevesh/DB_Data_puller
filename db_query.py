import cx_Oracle
from pprint import pprint


class create_db_con():
    def __init__(self):
        self.user = "" #update credentials here
        self.passwd = ""
        self.db_url = "172.17.0.2:1521/xe"
        self.con = None
        self.cur = None
    
    def __enter__(self):
        cx_Oracle.init_oracle_client(lib_dir=r"/opt/oracle/instantclient_21_3/")
        self.con = cx_Oracle.connect(self.user, self.passwd, self.db_url)
        self.cur = self.con.cursor()
        return self

    def get_query_result(self, query):
        self.cur.execute(query)
        res = self.cur.fetchall()
        row_desc = [r[0] for r in self.cur.description]
        res_dict = dict(zip(row_desc, list(zip(*res))))
        return res_dict

    def __exit__(self, *args):
        self.cur.close()
        self.con.close()

query_set = [
    "SELECT TABLE_NAME FROM all_tables WHERE OWNER ='ADMIN'",
    """SELECT cols.table_name,cols.column_name
        FROM all_constraints cons 
        JOIN all_cons_columns cols 
        ON cons.constraint_name = cols.constraint_name
        AND cons.owner = cols.owner
        WHERE cons.constraint_type = 'P'
        AND cols.OWNER = 'ADMIN'
        AND cols.table_name = '{0}'""",
    "SELECT * FROM admin.{0} WHERE ID = {1}"
]

def make_query(index_: int, data: list) -> dict:
    with create_db_con() as res:
        if index_ == 2:
            query = query_set[index_].format(data[1],data[2])
        else:        
            query = query_set[index_].format(data[index_])
        print(query)
        return res.get_query_result(query)


def get_path_details(path: str) -> dict:
    print(path.split("/"))
    return make_query(len(path.split("/"))-1, path.split("/"))
