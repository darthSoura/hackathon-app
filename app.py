from flask import Flask, redirect, render_template, request, jsonify, url_for, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, and_
import datetime
import calendar
import os

app = Flask(__name__)

ENV = 'dev'

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pcnlapgztfkwzf:6b0b6fcf74289f952310cb8e73ed0169db3bcf7615357d19c7c3b737d3115de2@ec2-3-217-14-181.compute-1.amazonaws.com:5432/dala58paf6m535'

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
        hackathons.append({'title':hack.project_name, 'prob_stat': hack.prob_stat, 'desc': hack.solution, 'techstacks': hack.techstacks, 'potential': hack.potential, 'hack_details': hack.hack_details, 'date': date, 
        'developers':hack.developers, 'repo_url':hack.repo_url, 'domain': hack.domain, 'theme': hack.theme})
    
    hackathons = hackathons[:10]
    return jsonify({'hackathons': hackathons})

@app.route('/index')
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/months")
@app.route("/months/")
def month():
    
    return render_template("months.html")

@app.route('/api/months/<string:yyyymm>')
def months(yyyymm):
    
    year = int(yyyymm[:-2])
    month = int(yyyymm[-2:])

    num_days = calendar.monthrange(year, month)[1]
    start_date = datetime.date(year, month, 1)
    end_date = datetime.date(year, month, num_days)
    
    hacks_list = Hacks.query.filter(
        and_(Hacks.date >= start_date, Hacks.date <= end_date)).all()
    
    return jsonify_hacks_list(hacks_list)
   
@app.route('/domains')
@app.route('/domains/')
def domain():
    return render_template("domains.html")

@app.route('/api/domains/<string:domain>')
def domains(domain): 
    hacks_list = Hacks.query.filter(Hacks.domain.ilike(domain))
    
    return jsonify_hacks_list(hacks_list)

@app.route('/themes')
@app.route('/themes/')
def theme():
    return render_template("themes.html")

@app.route('/api/themes/<string:theme>')
def themes(theme):
    hacks_list = Hacks.query.filter(Hacks.theme.ilike(theme))
    return jsonify_hacks_list(hacks_list)


if __name__== '__main__':
    app.run(host = "0.0.0.0", port=os.environ['PORT'])
