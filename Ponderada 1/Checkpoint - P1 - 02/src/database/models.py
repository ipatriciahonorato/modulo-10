from sqlalchemy import Column, Integer, String
from database.database import db

class User(db.Model):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False)
  password = Column(String(50), nullable=False)

  def __repr__(self):
    return f'<User:[id:{self.id}, name:{self.name}, email:{self.email}, password:{self.password}]>'
  
  def serialize(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
      "password": self.password
      }
  
class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    is_complete = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Task {self.title}>'

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'is_complete': self.is_complete,
            'user_id': self.user_id
        }