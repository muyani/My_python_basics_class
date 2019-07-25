from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@127.0.0.1:5432/taskmanager1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ssomesecerdfderere'
db = SQLAlchemy(app)
from models import TaskModel


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def hello_world():
    records = TaskModel.read_all()
    return render_template('index.html',records = records)

@app.route('/edit/<int:id>',methods=["POST"])
def edit(id):
    title = request.form['title']
    description = request.form['description']
    startdate = request.form['startdate']
    enddate = request.form['enddate']
    status = request.form['status']
    TaskModel.updateById(id=id,newtitle=title,newdescription=description,newstartdate=startdate,newenddate=enddate,newstatus=status)
    return redirect(url_for('hello_world'))


@app.route('/new',methods = ["POST"])
def newTask():
    if request.method == "POST":
        title = request.form['title']
        description= request.form['description']
        startdate = request.form['startdate']
        enddate= request.form['enddate']
        status = request.form['status']
        # try:
        newtask = TaskModel(title=title, description=description, startdate=startdate, enddate=enddate, status=status)
        newtask.insert()
        return redirect(url_for('hello_world'))
        # # except:
        #     flash("Failed to insert,database connection error")
        #     print("failed")
        #     return redirect(url_for('hello_world'))


    return render_template('index.html')





if __name__ == '__main__':
    app.run()
