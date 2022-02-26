from make_sql_connection import MakeSqlConnection
from database_work import DatabaseWork
from dotenv import load_dotenv
import os

load_dotenv()

database = 'MicrosoftDynamicsAX'
username = 'sa'
password = os.getenv('PASSWORD')
table_name = 'dbo.RETAILTRANSACTIONTABLE'

dbwork = DatabaseWork(database, table_name, username, password)

dbwork.execute()



