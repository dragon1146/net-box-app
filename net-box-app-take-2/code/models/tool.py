from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ToolModel(db.Model):

    __tablename__ = 'net_box'

    id = db.Column(db.Integer, primary_key=True)
    manufacture = db.Column(db.Text)
    device = db.Column(db.Text)
    task = db.Column(db.Text)
    command = db.Column(db.Text)
    notes = db.Column(db.Text)


    def __init__(self, manufacture, device, task, command, notes):
        self.manufacture = manufacture
        self.device = device
        self.task = task
        self.command = command
        self.notes = notes

    # def json(self):
    #   return {'id':self.id, 'name':self.name, 'contact':self.contact}

    @classmethod
    def find_tool_by_task(cls, task):
        return cls.query.filter_by(task=task).first()

    def add_tool_to_db(self):
        db.session.add(self)
        db.session.commit()
        return ToolModel.query.filter_by(task=self.task).first()

        