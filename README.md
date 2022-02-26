# workwithsql
📚 This repository helps to work with SQL server databases

During working on SQL master database, I have received several database backup which I should make data pipeline. 
For implementing a data pipeline, there is a demand to make new records for entire databse and it will be stunning task if 
someone has to make **insert** into SQL table for more than hundreds of columns.
This code make it simple.

## How to work:
just need implement some variables:

```python
database = 'sql server database name'
username = 'sql server username'
password = 'sql server password'
table_name = 'sql server table name'
```
then:
```python
from database_work import DatabaseWork
```
inside your code body implement:
```python
dbwork = DatabaseWork(database, table_name, username, password)
```
then:
```python
dbwork.execute()
```
it will bring new record to your existing database.

consider that if your table has `primary_key`, this code will not work.

I am working on it that bring new records for tables with `PK`.

**Thanks**
