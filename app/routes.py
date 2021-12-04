import sqlalchemy
from flask import request, render_template, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import and_
from sqlalchemy.orm import aliased
from sqlalchemy.sql.functions import concat, sysdate, func
from werkzeug.utils import redirect

from app import app, db
from app.models import User, TeamsFranchise, Team, People, Appearance, Batting, BattingPost, Pitching, PitchingPost, \
    SeriesPost


@app.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('standings'))
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm']
        if password != confirm:
            flash('Passwords don\'t match')
            return redirect(url_for('register'))
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists')
            return redirect(url_for('register'))
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('standings'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('standings'))
        else:
            return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('standings'))


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


# SELECT t.teamID, t.name, t.teamRank, t.W, t.L, t.DivWIn, t.WCWin, t.LgWin, t.WSWin, t.div_ID,
# (-(t.W - FIRST_VALUE(t.W) over (partition by t.div_ID order by t.teamRank asc)) +
# (t.L - FIRST_VALUE(t.L) over (partition by t.div_ID order by t.teamRank asc))) / 2 as GB
# FROM teams t
# WHERE t.yearID = 2020 ORDER BY t.div_ID, t.teamRank ASC;
def query_regular_standings(year: int):
    return db.session.query(Team).filter(Team.yearID == year) \
        .with_entities(Team.name, Team.lgID, Team.divID, Team.W, Team.L, Team.DivWin,
                       Team.WCWin, Team.LgWin, Team.WSWin,
                       ((Team.L - func.first_value(Team.L).over(partition_by=Team.div_ID,
                                                                order_by=Team.teamRank.asc())) -
                        (Team.W - func.first_value(Team.W).over(partition_by=Team.div_ID,
                                                                order_by=Team.teamRank.asc()))).label('GB')
                       ) \
        .all()


def query_playoffs_standings(year: int):
    team_win = aliased(Team)
    team_lost = aliased(Team)
    return db.session.query(SeriesPost).filter(SeriesPost.yearID == year) \
        .join(team_win, SeriesPost.team_IDwinner == team_win.ID) \
        .join(team_lost, SeriesPost.team_IDloser == team_lost.ID) \
        .with_entities(SeriesPost.round, team_win.name, team_lost.name, SeriesPost.wins, SeriesPost.losses,
                       SeriesPost.ties).all()


@app.route('/standings', methods=['GET', 'POST'])
@login_required
def standings():
    if 'year' not in request.form:
        selected_year = 2020
    else:
        selected_year = request.form['year']
    if 'season' not in request.form or request.form['season'] == 'regular':
        regular_standings = query_regular_standings(selected_year)
        playoffs_standings = None
    else:
        regular_standings = None
        playoffs_standings = query_playoffs_standings(selected_year)
    return render_template('standings.html', title='Standings', selected_year=selected_year,
                           regular_standings=regular_standings, playoffs_standings=playoffs_standings)


def query_rosters(team_id: str, year: int):
    return db.session.query(Appearance) \
        .join(Team, Appearance.team_ID == Team.ID) \
        .join(People, Appearance.playerID == People.playerID) \
        .filter(and_(Team.teamID == team_id, Team.yearID == year)) \
        .with_entities(concat(People.nameLast, ' ', People.nameGiven, ' ', People.nameFirst).label('NAME'),
                       (sqlalchemy.func.year(sysdate()) - sqlalchemy.func.year(People.birth_date)).label('AGE'),
                       concat(People.birthCity, ' ', People.birthState, ', ', People.birthCountry).label('BIRTH_PLACE'),
                       People.playerID).all()


def query_hitters(team_id: str, year: int):
    hitter_regular = db.session.query(Batting) \
        .join(Team, Batting.team_ID == Team.ID) \
        .join(People, Batting.playerID == People.playerID) \
        .filter(and_(Team.teamID == team_id, Team.yearID == year)) \
        .with_entities(Batting.playerID)
    hitter_post = db.session.query(BattingPost) \
        .join(Team, BattingPost.team_ID == Team.ID) \
        .join(People, BattingPost.playerID == People.playerID) \
        .filter(and_(Team.teamID == team_id, Team.yearID == year)) \
        .with_entities(BattingPost.playerID)
    hitter = hitter_regular.union(hitter_post)
    hitters = [x[0] for x in hitter.all()]
    return hitters


def query_pitchers(team_id: str, year: int):
    pitcher_regular = db.session.query(Pitching) \
        .join(Team, Pitching.team_ID == Team.ID) \
        .join(People, Pitching.playerID == People.playerID) \
        .filter(and_(Team.teamID == team_id, Team.yearID == year)) \
        .with_entities(Pitching.playerID)
    pitcher_post = db.session.query(PitchingPost) \
        .join(Team, PitchingPost.team_ID == Team.ID) \
        .join(People, PitchingPost.playerID == People.playerID) \
        .filter(and_(Team.teamID == team_id, Team.yearID == year)) \
        .with_entities(PitchingPost.playerID)
    pitcher = pitcher_regular.union(pitcher_post)
    pitchers = [x[0] for x in pitcher.all()]
    return pitchers


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    current_team = TeamsFranchise.query.filter(
        and_(TeamsFranchise.franchID == current_user.teamId, TeamsFranchise.active == 'Y')).first()
    teams_franchises = TeamsFranchise.query.filter_by(active='Y').all()
    if 'year' not in request.form:
        selected_year = 2020
    else:
        selected_year = request.form['year']
    rosters = query_rosters(current_user.teamId, selected_year)
    hitters = query_hitters(current_user.teamId, selected_year)
    pitchers = query_pitchers(current_user.teamId, selected_year)
    return render_template('profile.html', title='My Profile', teams_franchises=teams_franchises,
                           selected_year=selected_year, current_team=current_team, rosters=rosters, hitters=hitters,
                           pitchers=pitchers)


@app.route('/favorite', methods=['POST'])
@login_required
def favorite():
    current_user.teamId = request.form['favorite']
    db.session.commit()
    return redirect(url_for('profile'))
