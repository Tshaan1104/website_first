
from sqlalchemy import create_engine,text
import pymysql

engine = create_engine('mysql+pymysql://root:XHTZVHoVvwBlLqjIEWSOCyzwpXaWwUHu@monorail.proxy.rlwy.net:51527/railway')



def load_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("select * from website_first.job"))
    jobs=[]
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

jj=load_jobs_from_db()
# print(jj)
