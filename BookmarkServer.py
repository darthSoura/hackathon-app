from flask import Flask, redirect, render_template, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, and_
import datetime
import calendar
import os

app = Flask(__name__)

ENV = 'dev'

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wtvuiupcdetxbq:b2574c8bba14c541bd2d6925a25d40ce3310d08cbd457aa637c3361ffc3396bf@ec2-52-205-61-230.compute-1.amazonaws.com:5432/datpsej79i6r5n'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app);
# database and model
class Hacks(db.Model):
    __tablename__ = 'hacks'
    project_name = db.Column(db.Text(), primary_key=True)
    prob_stat = db.Column(db.Text(), primary_key=True)
    solution = db.Column(db.Text())
    techstacks = db.Column(db.ARRAY(String(200)))
    potential = db.Column(db.Text())
    hack_details = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.today)
    developers = db.Column(db.ARRAY(String(200)))
    repo_url = db.Column(db.Text())
    domain = db.Column(db.String(200))
    theme = db.Column(db.String(200))
    
    def __init__(self, project_name, prob_stat, solution, techstacks, potential, hack_details, date, developers, repo_url, domain, theme):
        self.project_name = project_name
        self.prob_stat = prob_stat
        self.solution = solution
        self.techstacks = techstacks
        self.potential = potential
        self.hack_details = hack_details
        self.date = date
        self.developers = developers
        self.repo_url = repo_url
        self.domain = domain
        self.theme = theme
  
def jsonify_hacks_list(hacks_list):
    hackathons = []
    for hack in hacks_list:
        date = hack.date.strftime("%B") + " " + str(hack.date.year)
        hackathons.append({'project_name':hack.project_name, 'prob_stat': hack.prob_stat, 'solution': hack.solution, 'techstacks': hack.techstacks, 'potential': hack.potential, 'hack_details': hack.hack_details, 'date': date, 
        'developers':hack.developers, 'repo_url':hack.repo_url, 'domain': hack.domain, 'theme': hack.theme})
    
    return jsonify({'hackathons': hackathons})

@app.route('/')
def home():
    return "Hello There"

# default Month redirection
@app.route("/months")
@app.route("/months/")
def month():
    last_mon = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
    
    return redirect(url_for('months', yyyymm = last_mon.strftime("%Y%m")))

# dynamic Handling of Month
@app.route('/months/<string:yyyymm>')
def months(yyyymm):
    
    year = int(yyyymm[:-2])
    month = int(yyyymm[-2:])

    num_days = calendar.monthrange(year, month)[1]
    start_date = datetime.date(year, month, 1)
    end_date = datetime.date(year, month, num_days)
    
    hacks_list = Hacks.query.filter(
        and_(Hacks.date >= start_date, Hacks.date <= end_date)).all()
    
    return jsonify_hacks_list(hacks_list)
   
# default Domain redirection    
@app.route('/domains')
@app.route('/domains/')
def domain():
    return redirect(url_for('domains', domain = "web development"))

# dynamic Handling of domain
@app.route('/domains/<string:domain>')
def domains(domain): 
    print(domain)
    hacks_list = Hacks.query.filter(Hacks.domain.ilike(domain))
    
    return jsonify_hacks_list(hacks_list)

# default Theme redirection
@app.route('/themes')
@app.route('/themes/')
def theme():
    return redirect(url_for('themes', theme = "education"))

# dynamic Handling of Theme
@app.route('/themes/<string:theme>')
def themes(theme):
    hacks_list = Hacks.query.filter(Hacks.theme.ilike(theme))
    return jsonify_hacks_list(hacks_list)


if __name__== '__main__':
    app.run(host = "0.0.0.0", port=os.environ['PORT'])
