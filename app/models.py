from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=True, unique=True)
    password = db.Column(db.String(128))
    teamId = db.Column(db.String(3))

    def __repr__(self):
        return '<User {}, {}>'.format(self.id, self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class TeamsFranchise(db.Model):
    __tablename__ = 'teamsfranchises'
    franchID = db.Column(db.String(3), primary_key=True)
    franchName = db.Column(db.String(50))
    active = db.Column(db.String(1))
    NAassoc = db.Column(db.String(3))

    def __repr__(self):
        return '<TeamsFranchises {}, {}>'.format(self.franchID, self.franchName)


class People(db.Model):
    __tablename__ = 'people'
    playerID = db.Column(db.String(9), primary_key=True)
    birthYear = db.Column(db.Integer)
    birthMonth = db.Column(db.Integer)
    birthDay = db.Column(db.Integer)
    birthCountry = db.Column(db.String(255))
    birthState = db.Column(db.String(255))
    birthCity = db.Column(db.String(255))
    deathYear = db.Column(db.Integer)
    deathMonth = db.Column(db.Integer)
    deathDay = db.Column(db.Integer)
    deathCountry = db.Column(db.String(255))
    deathState = db.Column(db.String(255))
    deathCity = db.Column(db.String(255))
    nameFirst = db.Column(db.String(255))
    nameLast = db.Column(db.String(255))
    nameGiven = db.Column(db.String(255))
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    bats = db.Column(db.String(255))
    throws = db.Column(db.String(255))
    debut = db.Column(db.String(255))
    finalGame = db.Column(db.String(255))
    retroID = db.Column(db.String(255))
    bbrefID = db.Column(db.String(255))
    birth_date = db.Column(db.Date)
    debut_date = db.Column(db.Date)
    finalgame_date = db.Column(db.Date)
    death_date = db.Column(db.Date)

    def __repr__(self):
        return '<People {}, {}, {}, {}>'.format(self.playerID, self.nameLast, self.nameGiven, self.nameFirst)


class Team(db.Model):
    __tablename__ = 'teams'
    ID = db.Column(db.Integer, primary_key=True)
    yearID = db.Column(db.Integer)
    lgID = db.Column(db.String(2))
    teamID = db.Column(db.String(3))
    franchID = db.Column(db.String(3))
    divID = db.Column(db.String(1))
    div_ID = db.Column(db.String(11))
    teamRank = db.Column(db.Integer)
    G = db.Column(db.Integer)
    Ghome = db.Column(db.Integer)
    W = db.Column(db.Integer)
    L = db.Column(db.Integer)
    DivWin = db.Column(db.String(1))
    WCWin = db.Column(db.String(1))
    LgWin = db.Column(db.String(1))
    WSWin = db.Column(db.String(1))
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Team {}, {}, {}>'.format(self.ID, self.yearID, self.teamID)


class Appearance(db.Model):
    __tablename__ = 'appearances'
    ID = db.Column(db.Integer, primary_key=True)
    yearID = db.Column(db.Integer)
    lgID = db.Column(db.String(2))
    teamID = db.Column(db.String(3))
    team_ID = db.Column(db.Integer)
    playerID = db.Column(db.String(9))

    def __repr__(self):
        return '<Appearance {}, {}, {}, {}>'.format(self.ID, self.yearID, self.teamID, self.playerID)


class Batting(db.Model):
    __tablename__ = 'batting'
    ID = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.String(9))
    yearID = db.Column(db.Integer)
    teamID = db.Column(db.String(3))
    team_ID = db.Column(db.Integer)
    lgID = db.Column(db.String(2))


class BattingPost(db.Model):
    __tablename__ = 'battingpost'
    ID = db.Column(db.Integer, primary_key=True)
    yearID = db.Column(db.Integer)
    playerID = db.Column(db.String(9))
    teamID = db.Column(db.String(3))
    team_ID = db.Column(db.Integer)
    lgID = db.Column(db.String(2))


class Pitching(db.Model):
    __tablename__ = 'pitching'
    ID = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.String(9))
    yearID = db.Column(db.Integer)
    teamID = db.Column(db.String(3))
    team_ID = db.Column(db.Integer)
    lgID = db.Column(db.String(2))


class PitchingPost(db.Model):
    __tablename__ = 'pitchingpost'
    ID = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.String(9))
    yearID = db.Column(db.Integer)
    teamID = db.Column(db.String(3))
    team_ID = db.Column(db.Integer)
    lgID = db.Column(db.String(2))


class SeriesPost(db.Model):
    __tablename__ = 'seriespost'
    ID = db.Column(db.Integer, primary_key=True)
    yearID = db.Column(db.Integer)
    round = db.Column(db.String(5))
    teamIDwinner = db.Column(db.String(3))
    lgIDwinner = db.Column(db.String(2))
    team_IDwinner = db.Column(db.Integer)
    teamIDloser = db.Column(db.String(3))
    lgIDloser = db.Column(db.String(2))
    team_IDloser = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    ties = db.Column(db.Integer)
