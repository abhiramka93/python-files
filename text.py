"""db connection 
create a table in db
establish connection 
ip_address,domain_name,user_name,password, port_num"""

class DBConnection:
    database="mysql"
    def __init__(self,ip_address,user_name,password,port_number):
        self.port_number = port_number
        self.ip_address = ip_address
        self.user_name = user_name
        self.password = password
    def connect(self):
        print(f"connect to {self.ip_address} with {self.user_name} on {self.port_number} connected to {DBConnection.database}")
    @staticmethod
    def localtime():
        print("Its 12 o clock")
    @classmethod
    def change_db_name(cls,db_name):
        cls.database =db_name
connection=DBConnection("102.0.1.1","Abhiram",123321,443)
print(connection.port_number)
print(connection.user_name)
connection.connect()
connection.localtime()
#connection.change_db_name("postgres")
print(connection.database)