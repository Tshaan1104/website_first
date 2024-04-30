
import os
from sqlalchemy import create_engine,text
import pymysql #for pymysql we have used the poetry add pymysql and then poetry add pymsql@latest

my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret)
# with engine.connect() as conn:
#   result=conn.execute(text("select * from website_first.job"))
#   rows=result.all()
#   print(rows[0]._asdict())


def load_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("select * from website_first.job"))
    jobs=[]
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

# jj=load_jobs_from_db()
# print(jj)
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from website_first.job where id=:id"), {'id': id})
    rows=result.all()
    # print(rows[0]._asdict())
    if len(rows)==0:
      return None
    else:
      return rows[0]._asdict()


