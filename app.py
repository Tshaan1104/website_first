# print('hello world')


from flask import Flask,render_template,jsonify

app = Flask(__name__)

job=[
    {'id':1,'title':'Data Analyst','location':'Bengaluru,India','salary':'$30000'},
    {'id':2,'title':'Data Analyst','location':'Bengaluru,India','salary':'$30000'},  
    {'id':3,'title':'Frontend Engineer','location':'Bengaluru,India'},
    {'id':1,'title':'Data Analyst','location':'Bengaluru,India','salary':'$30000'},
    {'id':4,'title':'Data Analyst','location':'Bengaluru,India','salary':'$130000'}]


@app.route('/')
def hello_world():
    return render_template('home.html',jobs=job,world= 'singleton')

@app.route('/jobs')
def list_jobs():
    return jsonify(job)

print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)