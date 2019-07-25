from app import db

class TaskModel(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(500),nullable=True)
    startdate = db.Column(db.String(30),nullable=True)
    enddate = db.Column(db.String(30),nullable=True)
    status = db.Column(db.String(30),nullable=False)

    # CRUD
    # insert a record
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # read
    @classmethod
    def read_all(cls):
        return cls.query.all()

    # update
    @classmethod
    def updateById(cls,id,newtitle = None , newdescription = None , newstartdate = None,newenddate = None , newstatus = None ):
        record = cls.query.filter_by(id=id).first()
        if record:
            if newtitle:
                record.title = newtitle
            if newdescription:
                record.description = newdescription
            if newenddate:
                record.enddate = newenddate
            if newstartdate:
                record.startdate = newstartdate
            if newstatus:
                record.status = newstatus
            db.session.commit()
            return True
        else:
            return False

        # delete
    @classmethod
    def deleteById(cls,id):
        record = cls.query.filter_by(id = id)
        if record.first():
            record.delete()
            db.session.commit()
            return True
        else:
            return False
















