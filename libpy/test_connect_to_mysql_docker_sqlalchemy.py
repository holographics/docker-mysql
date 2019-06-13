from datetime import datetime
# from jsonify import jsonify
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from marshmallow import Schema, fields
from sqlalchemy.orm import sessionmaker

db_url = 'localhost:3333'
db_name = 'wordpress_db'
db_user = 'wpuser'
db_password = 'wpuser@'
address = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_url}/{db_name}'
# address = 'mysql://wpuser:wpuser@localhost:3333/wordpress_db'


engine = create_engine(address)
Session = sessionmaker(bind=engine)
Base = declarative_base()


print(dir(engine))
print(engine.table_names())


class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by

class Exam(Entity, Base):
    __tablename__ = 'exams'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description


class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()


def get_exams():
    # fetching from the database
    session = Session()
    exam_objects = session.query(Exam).all()

    print('...!!! got exam_objects: %s' % exam_objects)

    # transforming into JSON-serializable objects
    schema = ExamSchema(many=True)

    exams = schema.dump(exam_objects)
    print('...!!! got exams: %s' % str(exams))

    # serializing as JSON
    session.close()
    return exams.data
    # return jsonify(exams.data)


def add_exam(**kwargs):
    # mount exam object
    posted_exam = ExamSchema(only=('title', 'description')).load(kwargs)
    print('...posted exame: %s' % str(posted_exam))

    exam = Exam(created_by="HTTP post request", **posted_exam.data)
    print('... exame: %s' % str(posted_exam))

    # persist exam
    session = Session()
    print('... session: %s' % str(session))
    session.add(exam)
    print('... added. about to commit: %s' % str(session))
    session.commit()

    # return created exam
    print('... about to dump: %s' % str(session))
    # new_exam = ExamSchema().dump(exam).data
    print('... closing after dump: %s' % str(session))
    session.close()
    # return jsonify(new_exam), 201
    return exam 


schema = ExamSchema(many=True)
print('...%s' % str(schema))
print('...%s' % dir(schema))
# exit()

# schema = ExamSchema(only=('title', 'description')).load({'description': 'description value 5', 'title': 'title value 5'})
# print (str(schema.data))
# exam = Exam(created_by="HTTP post request", **schema.data)

# # persist exam
# session = Session()
# session.add(exam)
# session.commit()

# exam = add_exam(**{'description': 'description value 16', 'title': 'title value 16'})

kwargs = {'updated_at': '2019-06-09T19:36:55+00:00', 
            'title': 'SQLAlchemy Exam 23', 
            'created_at': '2019-06-09T19:36:55+00:00', 
            'description': 'Test your knowledge about SQLAlchemy 23', 
            'last_updated_by': 
            'script 3'}


exam = add_exam(**kwargs)


print('.................exam..%s' % exam)
print('.................exam..%s' % dir(exam))

exams = get_exams()
print('.................exam 2..%s' % exam)
print('.................exam 2..%s' % dir(exam))
# new_exam = ExamSchema().dump(exam).data

# print('...............new_exam....%s' % new_exam)
# print('...............new_exam....%s' % dir(new_exam))
# # return created exam
# new_exam = ExamSchema().dump(exam).data
# session.close()
# return jsonify(new_exam), 201