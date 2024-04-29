
import os
from sqlalchemy import create_engine,text
import pymysql #for pymysql we have used the poetry add pymysql and then poetry add pymsql@latest

my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret)



def load_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("select * from website_first.job"))
    jobs=[]
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

jj=load_jobs_from_db()
# print(jj)
