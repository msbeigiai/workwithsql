from make_sql_connection import MakeSqlConnection
from database_work import DatabaseWork

database = 'MicrosoftDynamicsAX'
username = 'sa'
password = 'testpassword'
table_name = 'dbo.RETAILTRANSACTIONTABLE'

# make_connection = MakeSqlConnection(database, table_name, username, password)

command = (
   "INSERT INTO " + table_name + "(store_id, store_name, store_address, store_sell) "
   "VALUES (?, ?, ?, ?)"
)
data = (6632, "Mohsen", "Sattarkhan", 12365)

dbwork = DatabaseWork(database, table_name, username, password)

dbwork.execute()



