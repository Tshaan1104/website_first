
from sqlalchemy import create_engine,text
import pymysql
engine = create_engine('mysql+pymysql://root:XHTZVHoVvwBlLqjIEWSOCyzwpXaWwUHu@monorail.proxy.rlwy.net:51527/railway')

# with engine.connect() as conn:
#   result = conn.execute(text("select * from website_first.job"))
#   result_all=result.all()
#   # print(type(result.all[0])
#   # first_result_dict=result_all[0]._asdict()  #_asdict for the conversion of dictionary
#   result_dicts=[]
#   for row in result_all:
#     result_dicts.append(row._asdict())  #_asdict for the conversion to the dictionary

# print(result_dicts,end="/n")


def load_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("select * from website_first.job"))
    jobs=[]
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

jj=load_jobs_from_db()
# print(jj)
