import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="todo_app_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])


c = conn.cursor()

# table creation
c.execute('create table task_list (id serial, name varchar(255), primary key(id));')
c.execute('create table task(id serial, name varchar(255) NOT NULL, list_id int, primary key(id), foreign key(list_id) references list(id));')

# insert records
c.execute('insert into task_list (name) values ("pogrzeb wujka Stefana");')
c.execute('insert into task_list (name) values ("ślub");')
c.execute('insert into task (name, list_id) values ("kupić kwiaty", 1);')
c.execute('insert into task (name, list_id) values ("wyprać garnitur", 1);')
c.execute('insert into task (name, list_id) values ("wysłać zaproszenia", 2);')
c.execute('insert into task (name, list_id) values ("załatwić zespół", 2);')


conn.commit()

c.close()
conn.close()
