import pymysql
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:shadow123@localhost/publications')
import pandas as pd
data = pd.read_sql_query('SELECT * FROM employee', engine)
print(data.head())

import pymysql.cursors
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='password',
                             db='publications',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
q1 = '''
drop table Results1;
'''
cursor.execute(q1)
q1 = '''
create table Results1
select sales.stor_id, count(title_id) as Items, count(distinct(sales.`ord_num`)) as NumberofOrders, 
SUM(sales.qty) as QuantitySold, stores.stor_name as StoreName
From sales
left join stores 
on sales.stor_id = stores.stor_id
group by sales.stor_id
order by SUM(sales.qty);
'''
cursor.execute(q1)
x = cursor.fetchall()
data = pd.DataFrame(x)
data.head()