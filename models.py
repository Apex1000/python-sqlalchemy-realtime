from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'my_users'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    email = Column(String(120))
    password = Column(String(80))

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % (self.name)


class Users(Base):
    __tablename__ = 'user_data'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    username = Column(String(80))
    phone = Column(String(120))
    coine = Column(Integer)
    password = Column(String(120))


    def __init__(self, name=None,username=None,phone=None,coine=None,password=None):
        self.name = name
        self.username = username
        self.phone = phone
        self.coine = coine
        self.password = password

    def __repr__(self):
        return '<Users %r>' % (self.name)

class Bids(Base):
    __tablename__ = 'bids_data'

    id = Column(Integer, primary_key=True)
    bids_team1 = Column(String(80))
    bids_team2 = Column(String(80))
    rate = Column(String(80))
    baaw_team1 = Column(String(80))
    baaw_team2 = Column(String(80))

    def __init__(self, bids_team1=None,bids_team2=None, rate=None, baaw_team1=None, baaw_team2=None):
        self.bids_team1 = bids_team1
        self.bids_team2 = bids_team2
        self.rate = rate
        self.baaw_team1 = baaw_team1
        self.baaw_team2 = baaw_team2
    
    def __repr__(self):
        return '<Bids %r>' % (self.bids_team1)

class User_bids(Base):
    __tablename__ = 'user_bids'

    id = Column(Integer,primary_key=True)
    team_name = Column(String(80))
    baaw_rate = Column(String(80))
    coine = Column(String(80))
    user_id = Column(String(80))

    def __init__(self, team_name=None,baaw_rate=None,coine=None,user_id=None):
        self.team_name = team_name
        self.baaw_rate = baaw_rate
        self.coine = coine
        self.user_id = user_id
    
    def __repr__(self):
        return '<User_bids %r>' % (self.team_name)
