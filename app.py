# print('hello world')

from flask import Flask, render_template, jsonify,request
from flask.wrappers import Request
from sqlalchemy import text
from database import load_jobs_from_db, load_job_from_db,add_data_to_db

app = Flask(__name__)

# job=[
#     {'id':1,'title':'Data Analyst','location':'Bengaluru,India','salary':'$30000'},
#     {'id':2,'title':'Data Analyst','location':'Bengaluru,India','salary':'$30000'},
#     {'id':3,'title':'Frontend Engineer','location':'Bengaluru,India'},
#     {'id':1,'title':'Data Analyst','location':'Bengaluru,India','salary':'$30000'},
#     {'id':4,'title':'Data Analyst','location':'Bengaluru,India','salary':'$130000'}]


@app.route('/')
def hello_world():
  job = load_jobs_from_db()
  return render_template('home.html', jobs=job, world='singleton')


@app.route('/jobs')
def list_jobs():
  job = load_jobs_from_db()
  return jsonify(job)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found"
  return render_template('job_page.html', jobs=job)

@app.route("/job/<id>/apply", methods=['POST'])
def apply_job(id):
  data=request.form
  job=load_job_from_db(id)
  add_data_to_db(id,data)
  return render_template('application_submitted.html',application=data,jobs=job)

print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
