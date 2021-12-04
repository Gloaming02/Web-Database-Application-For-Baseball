import mysql.connector
import sys
import csv
import csi3335fall2021
from werkzeug.security import generate_password_hash, check_password_hash


def import_data_people(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('People.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                try:
                    row['birthYear'] = int(row['birthYear'])
                except (RuntimeError, TypeError, NameError):
                    row['birthYear'] = None
                try:
                    row['birthMonth'] = int(row['birthMonth'])
                except (RuntimeError, TypeError, NameError):
                    row['birthMonth'] = None
                try:
                    row['birthDay'] = int(row['birthDay'])
                except (RuntimeError, TypeError, NameError):
                    row['birthDay'] = None
                try:
                    row['deathYear'] = int(row['deathYear'])
                except (RuntimeError, TypeError, NameError):
                    row['deathYear'] = None
                try:
                    row['deathMonth'] = int(row['deathMonth'])
                except (RuntimeError, TypeError, NameError):
                    row['deathMonth'] = None
                try:
                    row['deathDay'] = int(row['deathDay'])
                except (RuntimeError, TypeError, NameError):
                    row['deathDay'] = None
                try:
                    row['weight'] = int(row['weight'])
                except (RuntimeError, TypeError, NameError):
                    row['weight'] = None
                try:
                    row['height'] = int(row['height'])
                except (RuntimeError, TypeError, NameError):
                    row['height'] = None
                if row['birthYear'] is not None and row['birthMonth'] is not None and row['birthDay'] is not None:
                    row['birth_date'] = '%04d-%02d-%02d' % (int(row['birthYear']), int(row['birthMonth']), int(row['birthDay']))
                else:
                    row['birth_date'] = None
                if row['debut'] is not None and row['debut'] != '':
                    row['debut_date'] = row['debut']
                else:
                    row['debut_date'] = None
                if row['finalGame'] is not None and row['finalGame'] != '':
                    row['finalgame_date'] = row['finalGame']
                else:
                    row['finalgame_date'] = None
                if row['deathYear'] is not None and row['deathMonth'] is not None and row['deathDay'] is not None:
                    row['death_date'] = '%04d-%02d-%02d' % (int(row['deathYear']), int(row['deathMonth']), int(row['deathDay']))
                else:
                    row['death_date'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO people VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing people to MariaDB Platform: {e}")


def import_data_awardsmanagers(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('AwardsManagers.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO awardsmanagers(playerID, awardID, yearID, lgID, tie, notes) VALUES(%s, %s, "
                        "%s, %s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing awardsmanagers to MariaDB Platform: {e}")


def import_data_awardsplayers(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('AwardsPlayers.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO awardsplayers(playerID, awardID, yearID, lgID, tie, notes) VALUES(%s, %s, "
                        "%s, %s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing awardsplayers to MariaDB Platform: {e}")


def import_data_awardssharemanagers(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('AwardsShareManagers.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['pointsWon'] = int(row['pointsWon'])
                except (RuntimeError, TypeError, NameError):
                    row['pointsWon'] = None
                try:
                    row['pointsMax'] = int(row['pointsMax'])
                except (RuntimeError, TypeError, NameError):
                    row['pointsMax'] = None
                try:
                    row['votesFirst'] = int(row['votesFirst'])
                except (RuntimeError, TypeError, NameError):
                    row['votesFirst'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO awardssharemanagers(awardID, yearID, lgID, playerID, pointsWon, pointsMax, "
                        "votesFirst) VALUES(%s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing awardssharemanagers to MariaDB Platform: {e}")


def import_data_awardsshareplayers(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('AwardsSharePlayers.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['pointsWon'] = float(row['pointsWon'])
                except (RuntimeError, TypeError, NameError):
                    row['pointsWon'] = None
                try:
                    row['pointsMax'] = int(row['pointsMax'])
                except (RuntimeError, TypeError, NameError):
                    row['pointsMax'] = None
                try:
                    row['votesFirst'] = float(row['votesFirst'])
                except (RuntimeError, TypeError, NameError):
                    row['votesFirst'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO awardsshareplayers(awardID, yearID, lgID, playerID, pointsWon, pointsMax, "
                        "votesFirst) VALUES(%s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing awardsshareplayers to MariaDB Platform: {e}")


def import_data_teamsfranchises(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('TeamsFranchises.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                if row['active'] == 'NA':
                    row['active'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO teamsfranchises VALUES(%s, %s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing teamsfranchises to MariaDB Platform: {e}")


def import_data_teams(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('Teams.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['Rank'] = int(row['Rank'])
                except (RuntimeError, TypeError, NameError):
                    row['Rank'] = None
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                try:
                    row['Ghome'] = int(row['Ghome'])
                except (RuntimeError, TypeError, NameError):
                    row['Ghome'] = None
                try:
                    row['W'] = int(row['W'])
                except (RuntimeError, TypeError, NameError):
                    row['W'] = None
                try:
                    row['L'] = int(row['L'])
                except (RuntimeError, TypeError, NameError):
                    row['L'] = None
                try:
                    row['R'] = int(row['R'])
                except (RuntimeError, TypeError, NameError):
                    row['R'] = None
                try:
                    row['AB'] = int(row['AB'])
                except (RuntimeError, TypeError, NameError):
                    row['AB'] = None
                try:
                    row['H'] = int(row['H'])
                except (RuntimeError, TypeError, NameError):
                    row['H'] = None
                try:
                    row['2B'] = int(row['2B'])
                except (RuntimeError, TypeError, NameError):
                    row['2B'] = None
                try:
                    row['3B'] = int(row['3B'])
                except (RuntimeError, TypeError, NameError):
                    row['3B'] = None
                try:
                    row['HR'] = int(row['HR'])
                except (RuntimeError, TypeError, NameError):
                    row['HR'] = None
                try:
                    row['BB'] = int(row['BB'])
                except (RuntimeError, TypeError, NameError):
                    row['BB'] = None
                try:
                    row['SO'] = int(row['SO'])
                except (RuntimeError, TypeError, NameError):
                    row['SO'] = None
                try:
                    row['SB'] = int(row['SB'])
                except (RuntimeError, TypeError, NameError):
                    row['SB'] = None
                try:
                    row['CS'] = int(row['CS'])
                except (RuntimeError, TypeError, NameError):
                    row['CS'] = None
                try:
                    row['HBP'] = int(row['HBP'])
                except (RuntimeError, TypeError, NameError):
                    row['HBP'] = None
                try:
                    row['SF'] = int(row['SF'])
                except (RuntimeError, TypeError, NameError):
                    row['SF'] = None
                try:
                    row['RA'] = int(row['RA'])
                except (RuntimeError, TypeError, NameError):
                    row['RA'] = None
                try:
                    row['ER'] = int(row['ER'])
                except (RuntimeError, TypeError, NameError):
                    row['ER'] = None
                try:
                    row['ERA'] = float(row['ERA'])
                except (RuntimeError, TypeError, NameError):
                    row['ERA'] = None
                try:
                    row['CG'] = int(row['CG'])
                except (RuntimeError, TypeError, NameError):
                    row['CG'] = None
                try:
                    row['SHO'] = int(row['SHO'])
                except (RuntimeError, TypeError, NameError):
                    row['SHO'] = None
                try:
                    row['SV'] = int(row['SV'])
                except (RuntimeError, TypeError, NameError):
                    row['SV'] = None
                try:
                    row['IPouts'] = int(row['IPouts'])
                except (RuntimeError, TypeError, NameError):
                    row['IPouts'] = None
                try:
                    row['HA'] = int(row['HA'])
                except (RuntimeError, TypeError, NameError):
                    row['HA'] = None
                try:
                    row['HRA'] = int(row['HRA'])
                except (RuntimeError, TypeError, NameError):
                    row['HRA'] = None
                try:
                    row['BBA'] = int(row['BBA'])
                except (RuntimeError, TypeError, NameError):
                    row['BBA'] = None
                try:
                    row['SOA'] = int(row['SOA'])
                except (RuntimeError, TypeError, NameError):
                    row['SOA'] = None
                try:
                    row['E'] = int(row['E'])
                except (RuntimeError, TypeError, NameError):
                    row['E'] = None
                try:
                    row['DP'] = int(row['DP'])
                except (RuntimeError, TypeError, NameError):
                    row['DP'] = None
                try:
                    row['FP'] = float(row['FP'])
                except (RuntimeError, TypeError, NameError):
                    row['FP'] = None
                try:
                    row['attendance'] = int(row['attendance'])
                except (RuntimeError, TypeError, NameError):
                    row['attendance'] = None
                try:
                    row['BPF'] = int(row['BPF'])
                except (RuntimeError, TypeError, NameError):
                    row['BPF'] = None
                try:
                    row['PPF'] = int(row['PPF'])
                except (RuntimeError, TypeError, NameError):
                    row['PPF'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO teams(yearID, lgID, teamID, franchID, divID, teamRank, G, Ghome, W, L, "
                        "DivWin, WCWin, LgWin, WSWin, R, AB, H, 2B, 3B, HR, BB, SO, SB, CS, HBP, SF, RA, ER, ERA, "
                        "CG, SHO, SV, IPouts, HA, HRA, BBA, SOA, E, DP, FP, name, park, attendance, BPF, PPF, "
                        "teamIDBR, teamIDlahman45, teamIDretro) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE teams t SET t.div_ID = (SELECT d.ID FROM divisions d WHERE d.divID = t.divID and d.lgID = "
                    "t.lgID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing teams to MariaDB Platform: {e}")


def import_data_teamshalf(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('TeamsHalf.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['Rank'] = int(row['Rank'])
                except (RuntimeError, TypeError, NameError):
                    row['Rank'] = None
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                try:
                    row['W'] = int(row['W'])
                except (RuntimeError, TypeError, NameError):
                    row['W'] = None
                try:
                    row['L'] = int(row['L'])
                except (RuntimeError, TypeError, NameError):
                    row['L'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO teamshalf(yearID, lgID, teamID, Half, divID, DivWin, teamRank, G, W, "
                        "L) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE teamshalf a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND "
                    "t.yearID = a.yearID AND t.teamID = a.teamID)")
        cur.execute("UPDATE teamshalf t SET t.div_ID = (SELECT d.ID FROM divisions d WHERE d.divID = t.divID and "
                    "d.lgID = t.lgID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing teamshalf to MariaDB Platform: {e}")


def import_data_seriespost(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('SeriesPost.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['wins'] = int(row['wins'])
                except (RuntimeError, TypeError, NameError):
                    row['wins'] = None
                try:
                    row['losses'] = int(row['losses'])
                except (RuntimeError, TypeError, NameError):
                    row['losses'] = None
                try:
                    row['ties'] = int(row['ties'])
                except (RuntimeError, TypeError, NameError):
                    row['ties'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO seriespost(yearID, round, teamIDwinner, lgIDwinner, teamIDloser, lgIDloser, "
                        "wins, losses, ties) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE seriespost a SET a.team_IDwinner = (SELECT ID FROM teams t WHERE t.lgID = a.lgIDwinner AND "
                    "t.yearID = a.yearID AND t.teamID = a.teamIDwinner)")
        cur.execute("UPDATE seriespost a SET a.team_IDloser = (SELECT ID FROM teams t WHERE t.lgID = a.lgIDloser AND "
                    "t.yearID = a.yearID AND t.teamID = a.teamIDloser)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing seriespost to MariaDB Platform: {e}")


def import_data_allstarfull(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('AllstarFull.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                try:
                    row['yearID'] = int(row['yearID'])
                except (RuntimeError, TypeError, NameError):
                    row['yearID'] = None
                try:
                    if row['gameNum'] is None:
                        continue
                    row['gameNum'] = int(row['gameNum'])
                except (RuntimeError, TypeError, NameError):
                    row['gameNum'] = None
                try:
                    row['GP'] = int(row['GP'])
                except (RuntimeError, TypeError, NameError):
                    row['GP'] = None
                try:
                    row['startingPos'] = int(row['startingPos'])
                except (RuntimeError, TypeError, NameError):
                    row['startingPos'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO allstarfull(playerID, yearID, gameNum, gameID, teamID, lgID, GP, "
                        "startingPos) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE allstarfull a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND t.yearID "
                    "= a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing allstarfull to MariaDB Platform: {e}")


def import_data_appearances(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('Appearances.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['G_all'] = int(row['G_all'])
                except (RuntimeError, TypeError, NameError):
                    row['G_all'] = None
                try:
                    row['GS'] = int(row['GS'])
                except (RuntimeError, TypeError, NameError):
                    row['GS'] = None
                try:
                    row['G_batting'] = int(row['G_batting'])
                except (RuntimeError, TypeError, NameError):
                    row['G_batting'] = None
                try:
                    row['G_defense'] = int(row['G_defense'])
                except (RuntimeError, TypeError, NameError):
                    row['G_defense'] = None
                try:
                    row['G_p'] = int(row['G_p'])
                except (RuntimeError, TypeError, NameError):
                    row['G_p'] = None
                try:
                    row['G_c'] = int(row['G_c'])
                except (RuntimeError, TypeError, NameError):
                    row['G_c'] = None
                try:
                    row['G_1b'] = int(row['G_1b'])
                except (RuntimeError, TypeError, NameError):
                    row['G_1b'] = None
                try:
                    row['G_2b'] = int(row['G_2b'])
                except (RuntimeError, TypeError, NameError):
                    row['G_2b'] = None
                try:
                    row['G_3b'] = int(row['G_3b'])
                except (RuntimeError, TypeError, NameError):
                    row['G_3b'] = None
                try:
                    row['G_ss'] = int(row['G_ss'])
                except (RuntimeError, TypeError, NameError):
                    row['G_ss'] = None
                try:
                    row['G_lf'] = int(row['G_lf'])
                except (RuntimeError, TypeError, NameError):
                    row['G_lf'] = None
                try:
                    row['G_cf'] = int(row['G_cf'])
                except (RuntimeError, TypeError, NameError):
                    row['G_cf'] = None
                try:
                    row['G_rf'] = int(row['G_rf'])
                except (RuntimeError, TypeError, NameError):
                    row['G_rf'] = None
                try:
                    row['G_of'] = int(row['G_of'])
                except (RuntimeError, TypeError, NameError):
                    row['G_of'] = None
                try:
                    row['G_dh'] = int(row['G_dh'])
                except (RuntimeError, TypeError, NameError):
                    row['G_dh'] = None
                try:
                    row['G_ph'] = int(row['G_ph'])
                except (RuntimeError, TypeError, NameError):
                    row['G_ph'] = None
                try:
                    row['G_pr'] = int(row['G_pr'])
                except (RuntimeError, TypeError, NameError):
                    row['G_pr'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO appearances(yearID, teamID, lgID, playerID, G_all, GS, G_batting, G_defense, "
                        "G_p, G_c, G_1b, G_2b, G_3b, G_ss, G_lf, G_cf, G_rf, G_of, G_dh, G_ph, G_pr) VALUES(%s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE appearances a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND t.yearID "
                    "= a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing appearances to MariaDB Platform: {e}")


def import_data_batting(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('Batting.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                row['stint'] = int(row['stint'])
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                # try:
                #     row['G_batting'] = int(row['G_batting'])
                # except (RuntimeError, TypeError, NameError):
                #     row['G_batting'] = None
                try:
                    row['AB'] = int(row['AB'])
                except (RuntimeError, TypeError, NameError):
                    row['AB'] = None
                try:
                    row['R'] = int(row['R'])
                except (RuntimeError, TypeError, NameError):
                    row['R'] = None
                try:
                    row['H'] = int(row['H'])
                except (RuntimeError, TypeError, NameError):
                    row['H'] = None
                try:
                    row['2B'] = int(row['2B'])
                except (RuntimeError, TypeError, NameError):
                    row['2B'] = None
                try:
                    row['3B'] = int(row['3B'])
                except (RuntimeError, TypeError, NameError):
                    row['3B'] = None
                try:
                    row['HR'] = int(row['HR'])
                except (RuntimeError, TypeError, NameError):
                    row['HR'] = None
                try:
                    row['RBI'] = int(row['RBI'])
                except (RuntimeError, TypeError, NameError):
                    row['RBI'] = None
                try:
                    row['SB'] = int(row['SB'])
                except (RuntimeError, TypeError, NameError):
                    row['SB'] = None
                try:
                    row['CS'] = int(row['CS'])
                except (RuntimeError, TypeError, NameError):
                    row['CS'] = None
                try:
                    row['BB'] = int(row['BB'])
                except (RuntimeError, TypeError, NameError):
                    row['BB'] = None
                try:
                    row['SO'] = int(row['SO'])
                except (RuntimeError, TypeError, NameError):
                    row['SO'] = None
                try:
                    row['IBB'] = int(row['IBB'])
                except (RuntimeError, TypeError, NameError):
                    row['IBB'] = None
                try:
                    row['HBP'] = int(row['HBP'])
                except (RuntimeError, TypeError, NameError):
                    row['HBP'] = None
                try:
                    row['SH'] = int(row['SH'])
                except (RuntimeError, TypeError, NameError):
                    row['SH'] = None
                try:
                    row['SF'] = int(row['SF'])
                except (RuntimeError, TypeError, NameError):
                    row['SF'] = None
                try:
                    row['GIDP'] = int(row['GIDP'])
                except (RuntimeError, TypeError, NameError):
                    row['GIDP'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO batting(playerID, yearID, stint, teamID, lgID, G, G_batting, AB, "
                        "R, H, 2B, 3B, HR, RBI, SB, CS, BB, SO, IBB, HBP, SH, SF, GIDP) VALUES(%s, "
                        "%s, %s, %s, %s, %s, NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        list(data))
        cur.execute("UPDATE batting a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND t.yearID "
                    "= a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing batting to MariaDB Platform: {e}")


def import_data_battingpost(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('BattingPost.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                try:
                    row['AB'] = int(row['AB'])
                except (RuntimeError, TypeError, NameError):
                    row['AB'] = None
                try:
                    row['R'] = int(row['R'])
                except (RuntimeError, TypeError, NameError):
                    row['R'] = None
                try:
                    row['H'] = int(row['H'])
                except (RuntimeError, TypeError, NameError):
                    row['H'] = None
                try:
                    row['2B'] = int(row['2B'])
                except (RuntimeError, TypeError, NameError):
                    row['2B'] = None
                try:
                    row['3B'] = int(row['3B'])
                except (RuntimeError, TypeError, NameError):
                    row['3B'] = None
                try:
                    row['HR'] = int(row['HR'])
                except (RuntimeError, TypeError, NameError):
                    row['HR'] = None
                try:
                    row['RBI'] = int(row['RBI'])
                except (RuntimeError, TypeError, NameError):
                    row['RBI'] = None
                try:
                    row['SB'] = int(row['SB'])
                except (RuntimeError, TypeError, NameError):
                    row['SB'] = None
                try:
                    row['CS'] = int(row['CS'])
                except (RuntimeError, TypeError, NameError):
                    row['CS'] = None
                try:
                    row['BB'] = int(row['BB'])
                except (RuntimeError, TypeError, NameError):
                    row['BB'] = None
                try:
                    row['SO'] = int(row['SO'])
                except (RuntimeError, TypeError, NameError):
                    row['SO'] = None
                try:
                    row['IBB'] = int(row['IBB'])
                except (RuntimeError, TypeError, NameError):
                    row['IBB'] = None
                try:
                    row['HBP'] = int(row['HBP'])
                except (RuntimeError, TypeError, NameError):
                    row['HBP'] = None
                try:
                    row['SH'] = int(row['SH'])
                except (RuntimeError, TypeError, NameError):
                    row['SH'] = None
                try:
                    row['SF'] = int(row['SF'])
                except (RuntimeError, TypeError, NameError):
                    row['SF'] = None
                try:
                    row['GIDP'] = int(row['GIDP'])
                except (RuntimeError, TypeError, NameError):
                    row['GIDP'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO battingpost(yearID, round, playerID, teamID, lgID, G, AB, "
                        "R, H, 2B, 3B, HR, RBI, SB, CS, BB, SO, IBB, HBP, SH, SF, GIDP) VALUES(%s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE battingpost a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND t.yearID "
                    "= a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing battingpost to MariaDB Platform: {e}")


def import_data_fielding(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('Fielding.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                try:
                    row['GS'] = int(row['GS'])
                except (RuntimeError, TypeError, NameError):
                    row['GS'] = None
                try:
                    row['InnOuts'] = int(row['InnOuts'])
                except (RuntimeError, TypeError, NameError):
                    row['InnOuts'] = None
                try:
                    row['PO'] = int(row['PO'])
                except (RuntimeError, TypeError, NameError):
                    row['PO'] = None
                try:
                    row['A'] = int(row['A'])
                except (RuntimeError, TypeError, NameError):
                    row['A'] = None
                try:
                    row['E'] = int(row['E'])
                except (RuntimeError, TypeError, NameError):
                    row['E'] = None
                try:
                    row['DP'] = int(row['DP'])
                except (RuntimeError, TypeError, NameError):
                    row['DP'] = None
                try:
                    row['PB'] = int(row['PB'])
                except (RuntimeError, TypeError, NameError):
                    row['PB'] = None
                try:
                    row['WP'] = int(row['WP'])
                except (RuntimeError, TypeError, NameError):
                    row['WP'] = None
                try:
                    row['SB'] = int(row['SB'])
                except (RuntimeError, TypeError, NameError):
                    row['SB'] = None
                try:
                    row['CS'] = int(row['CS'])
                except (RuntimeError, TypeError, NameError):
                    row['CS'] = None
                try:
                    row['ZR'] = int(row['ZR'])
                except (RuntimeError, TypeError, NameError):
                    row['ZR'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO fielding(playerID, yearID, stint, teamID, lgID, POS, G, "
                        "GS, InnOuts, PO, A, E, DP, PB, WP, SB, CS, ZR) VALUES(%s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE fielding a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND t.yearID "
                    "= a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing fielding to MariaDB Platform: {e}")


def import_data_fieldingof(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('FieldingOF.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                row['stint'] = int(row['stint'])
                try:
                    row['Glf'] = int(row['Glf'])
                except (RuntimeError, TypeError, NameError):
                    row['Glf'] = None
                try:
                    row['Gcf'] = int(row['Gcf'])
                except (RuntimeError, TypeError, NameError):
                    row['Gcf'] = None
                try:
                    row['Grf'] = int(row['Grf'])
                except (RuntimeError, TypeError, NameError):
                    row['Grf'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO fieldingof(playerID, yearID, stint, Glf, Gcf, Grf) VALUES(%s, "
                        "%s, %s, %s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing fieldingof to MariaDB Platform: {e}")


def import_data_fieldingofsplit(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('FieldingOFsplit.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                try:
                    row['GS'] = int(row['GS'])
                except (RuntimeError, TypeError, NameError):
                    row['GS'] = None
                try:
                    row['InnOuts'] = int(row['InnOuts'])
                except (RuntimeError, TypeError, NameError):
                    row['InnOuts'] = None
                try:
                    row['PO'] = int(row['PO'])
                except (RuntimeError, TypeError, NameError):
                    row['PO'] = None
                try:
                    row['A'] = int(row['A'])
                except (RuntimeError, TypeError, NameError):
                    row['A'] = None
                try:
                    row['E'] = int(row['E'])
                except (RuntimeError, TypeError, NameError):
                    row['E'] = None
                try:
                    row['DP'] = int(row['DP'])
                except (RuntimeError, TypeError, NameError):
                    row['DP'] = None
                try:
                    row['PB'] = int(row['PB'])
                except (RuntimeError, TypeError, NameError):
                    row['PB'] = None
                try:
                    row['WP'] = int(row['WP'])
                except (RuntimeError, TypeError, NameError):
                    row['WP'] = None
                try:
                    row['SB'] = int(row['SB'])
                except (RuntimeError, TypeError, NameError):
                    row['SB'] = None
                try:
                    row['CS'] = int(row['CS'])
                except (RuntimeError, TypeError, NameError):
                    row['CS'] = None
                try:
                    row['ZR'] = int(row['ZR'])
                except (RuntimeError, TypeError, NameError):
                    row['ZR'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO fieldingofsplit(playerID, yearID, stint, teamID, lgID, POS, G, "
                        "GS, InnOuts, PO, A, E, DP, PB, WP, SB, CS, ZR) VALUES(%s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE fieldingofsplit a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND "
                    "t.yearID = a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing fieldingofsplit to MariaDB Platform: {e}")


def import_data_fieldingpost(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('FieldingPost.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                try:
                    row['GS'] = int(row['GS'])
                except (RuntimeError, TypeError, NameError):
                    row['GS'] = None
                try:
                    row['InnOuts'] = int(row['InnOuts'])
                except (RuntimeError, TypeError, NameError):
                    row['InnOuts'] = None
                try:
                    row['PO'] = int(row['PO'])
                except (RuntimeError, TypeError, NameError):
                    row['PO'] = None
                try:
                    row['A'] = int(row['A'])
                except (RuntimeError, TypeError, NameError):
                    row['A'] = None
                try:
                    row['E'] = int(row['E'])
                except (RuntimeError, TypeError, NameError):
                    row['E'] = None
                try:
                    row['DP'] = int(row['DP'])
                except (RuntimeError, TypeError, NameError):
                    row['DP'] = None
                try:
                    row['TP'] = int(row['TP'])
                except (RuntimeError, TypeError, NameError):
                    row['TP'] = None
                try:
                    row['PB'] = int(row['PB'])
                except (RuntimeError, TypeError, NameError):
                    row['PB'] = None
                try:
                    row['SB'] = int(row['SB'])
                except (RuntimeError, TypeError, NameError):
                    row['SB'] = None
                try:
                    row['CS'] = int(row['CS'])
                except (RuntimeError, TypeError, NameError):
                    row['CS'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO fieldingpost(playerID, yearID, teamID, lgID, round, POS, G, "
                        "GS, InnOuts, PO, A, E, DP, TP, PB, SB, CS) VALUES(%s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE fieldingpost a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND "
                    "t.yearID = a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing fieldingpost to MariaDB Platform: {e}")


def import_data_halloffame(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('HallOfFame.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['ballots'] = int(row['ballots'])
                except (RuntimeError, TypeError, NameError):
                    row['ballots'] = None
                try:
                    row['needed'] = int(row['needed'])
                except (RuntimeError, TypeError, NameError):
                    row['needed'] = None
                try:
                    row['votes'] = int(row['votes'])
                except (RuntimeError, TypeError, NameError):
                    row['votes'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO halloffame(playerID, yearID, votedBy, ballots, needed, votes, inducted, "
                        "category, needed_note) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing halloffame to MariaDB Platform: {e}")


def import_data_managers(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('Managers.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                row['inseason'] = int(row['inseason'])
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                try:
                    row['W'] = int(row['W'])
                except (RuntimeError, TypeError, NameError):
                    row['W'] = None
                try:
                    row['L'] = int(row['L'])
                except (RuntimeError, TypeError, NameError):
                    row['L'] = None
                try:
                    row['rank'] = int(row['rank'])
                except (RuntimeError, TypeError, NameError):
                    row['rank'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO managers(playerID, yearID, teamID, lgID, inseason, G, "
                        "W, L, teamRank, plyrMgr) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE managers a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND "
                    "t.yearID = a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing managers to MariaDB Platform: {e}")


def import_data_managershalf(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('ManagersHalf.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['inseason'] = int(row['inseason'])
                except (RuntimeError, TypeError, NameError):
                    row['inseason'] = None
                try:
                    row['half'] = int(row['half'])
                except (RuntimeError, TypeError, NameError):
                    row['half'] = None
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                try:
                    row['W'] = int(row['W'])
                except (RuntimeError, TypeError, NameError):
                    row['W'] = None
                try:
                    row['L'] = int(row['L'])
                except (RuntimeError, TypeError, NameError):
                    row['L'] = None
                try:
                    row['rank'] = int(row['rank'])
                except (RuntimeError, TypeError, NameError):
                    row['rank'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO managershalf(playerID, yearID, teamID, lgID, inseason, half, G, "
                        "W, L, teamRank) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE managershalf a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND "
                    "t.yearID = a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing managershalf to MariaDB Platform: {e}")


def import_data_parks(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('Parks.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO parks(parkkey, parkname, parkalias, city, state, country)"
                        " VALUES(%s, %s, %s, %s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing parks to MariaDB Platform: {e}")


def import_data_homegames(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('HomeGames.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                try:
                    row['year.key'] = int(row['year.key'])
                except (RuntimeError, TypeError, NameError):
                    row['year.key'] = None
                try:
                    row['games'] = int(row['games'])
                except (RuntimeError, TypeError, NameError):
                    row['games'] = None
                try:
                    row['openings'] = int(row['openings'])
                except (RuntimeError, TypeError, NameError):
                    row['openings'] = None
                try:
                    row['attendance'] = int(row['attendance'])
                except (RuntimeError, TypeError, NameError):
                    row['attendance'] = None
                if row['span.first'] is not None:
                    row['spanfirst_date'] = row['span.first']
                if row['span.last'] is not None:
                    row['spanlast_date'] = row['span.last']
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO homegames(yearkey, leaguekey, teamkey, parkkey, spanfirst, spanlast, games,"
                        "openings, attendance, spanfirst_date, spanlast_date) VALUES(%s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s)", list(data))
        cur.execute("UPDATE homegames a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.leaguekey AND "
                    "t.yearID = a.yearkey AND t.teamID = a.teamkey)")
        cur.execute("UPDATE homegames a SET a.park_ID = (SELECT ID FROM parks t WHERE t.parkkey = a.parkkey)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing homegames to MariaDB Platform: {e}")


def import_data_pitching(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('Pitching.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                row['stint'] = int(row['stint'])
                try:
                    row['W'] = int(row['W'])
                except (RuntimeError, TypeError, NameError):
                    row['W'] = None
                try:
                    row['L'] = int(row['L'])
                except (RuntimeError, TypeError, NameError):
                    row['L'] = None
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                try:
                    row['GS'] = int(row['GS'])
                except (RuntimeError, TypeError, NameError):
                    row['GS'] = None
                try:
                    row['GS'] = int(row['GS'])
                except (RuntimeError, TypeError, NameError):
                    row['GS'] = None
                try:
                    row['CG'] = int(row['CG'])
                except (RuntimeError, TypeError, NameError):
                    row['CG'] = None
                try:
                    row['SHO'] = int(row['SHO'])
                except (RuntimeError, TypeError, NameError):
                    row['SHO'] = None
                try:
                    row['SV'] = int(row['SV'])
                except (RuntimeError, TypeError, NameError):
                    row['SV'] = None
                try:
                    row['IPouts'] = int(row['IPouts'])
                except (RuntimeError, TypeError, NameError):
                    row['IPouts'] = None
                try:
                    row['H'] = int(row['H'])
                except (RuntimeError, TypeError, NameError):
                    row['H'] = None
                try:
                    row['ER'] = int(row['ER'])
                except (RuntimeError, TypeError, NameError):
                    row['ER'] = None
                try:
                    row['HR'] = int(row['HR'])
                except (RuntimeError, TypeError, NameError):
                    row['HR'] = None
                try:
                    row['BB'] = int(row['BB'])
                except (RuntimeError, TypeError, NameError):
                    row['BB'] = None
                try:
                    row['SO'] = int(row['SO'])
                except (RuntimeError, TypeError, NameError):
                    row['SO'] = None
                try:
                    row['BAOpp'] = float(row['BAOpp'])
                except (RuntimeError, TypeError, NameError):
                    row['BAOpp'] = None
                try:
                    row['ERA'] = float(row['ERA'])
                except (RuntimeError, TypeError, NameError):
                    row['ERA'] = None
                try:
                    row['IBB'] = int(row['IBB'])
                except (RuntimeError, TypeError, NameError):
                    row['IBB'] = None
                try:
                    row['WP'] = int(row['WP'])
                except (RuntimeError, TypeError, NameError):
                    row['WP'] = None
                try:
                    row['HBP'] = int(row['HBP'])
                except (RuntimeError, TypeError, NameError):
                    row['HBP'] = None
                try:
                    row['BK'] = int(row['BK'])
                except (RuntimeError, TypeError, NameError):
                    row['BK'] = None
                try:
                    row['BFP'] = int(row['BFP'])
                except (RuntimeError, TypeError, NameError):
                    row['BFP'] = None
                try:
                    row['GF'] = int(row['GF'])
                except (RuntimeError, TypeError, NameError):
                    row['GF'] = None
                try:
                    row['R'] = int(row['R'])
                except (RuntimeError, TypeError, NameError):
                    row['R'] = None
                try:
                    row['SH'] = int(row['SH'])
                except (RuntimeError, TypeError, NameError):
                    row['SH'] = None
                try:
                    row['SF'] = int(row['SF'])
                except (RuntimeError, TypeError, NameError):
                    row['SF'] = None
                try:
                    row['GIDP'] = int(row['GIDP'])
                except (RuntimeError, TypeError, NameError):
                    row['GIDP'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO pitching(playerID, yearID, stint, teamID, lgID, W, L, G, GS, CG, SHO, SV, "
                        "IPouts, H, ER, HR, BB, SO, BAOpp, ERA, IBB, WP, HBP, BK, BFP, GF, R, SH, SF, "
                        "GIDP) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE pitching a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND "
                    "t.yearID = a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing pitching to MariaDB Platform: {e}")


def import_data_pitchingpost(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('PitchingPost.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['W'] = int(row['W'])
                except (RuntimeError, TypeError, NameError):
                    row['W'] = None
                try:
                    row['L'] = int(row['L'])
                except (RuntimeError, TypeError, NameError):
                    row['L'] = None
                try:
                    row['G'] = int(row['G'])
                except (RuntimeError, TypeError, NameError):
                    row['G'] = None
                try:
                    row['GS'] = int(row['GS'])
                except (RuntimeError, TypeError, NameError):
                    row['GS'] = None
                try:
                    row['GS'] = int(row['GS'])
                except (RuntimeError, TypeError, NameError):
                    row['GS'] = None
                try:
                    row['CG'] = int(row['CG'])
                except (RuntimeError, TypeError, NameError):
                    row['CG'] = None
                try:
                    row['SHO'] = int(row['SHO'])
                except (RuntimeError, TypeError, NameError):
                    row['SHO'] = None
                try:
                    row['SV'] = int(row['SV'])
                except (RuntimeError, TypeError, NameError):
                    row['SV'] = None
                try:
                    row['IPouts'] = int(row['IPouts'])
                except (RuntimeError, TypeError, NameError):
                    row['IPouts'] = None
                try:
                    row['H'] = int(row['H'])
                except (RuntimeError, TypeError, NameError):
                    row['H'] = None
                try:
                    row['ER'] = int(row['ER'])
                except (RuntimeError, TypeError, NameError):
                    row['ER'] = None
                try:
                    row['HR'] = int(row['HR'])
                except (RuntimeError, TypeError, NameError):
                    row['HR'] = None
                try:
                    row['BB'] = int(row['BB'])
                except (RuntimeError, TypeError, NameError):
                    row['BB'] = None
                try:
                    row['SO'] = int(row['SO'])
                except (RuntimeError, TypeError, NameError):
                    row['SO'] = None
                try:
                    row['BAOpp'] = float(row['BAOpp'])
                except (RuntimeError, TypeError, NameError):
                    row['BAOpp'] = None
                try:
                    if row['ERA'] == 'inf':
                        row['ERA'] = None
                    else:
                        row['ERA'] = float(row['ERA'])
                except (RuntimeError, TypeError, NameError):
                    row['ERA'] = None
                try:
                    row['IBB'] = int(row['IBB'])
                except (RuntimeError, TypeError, NameError):
                    row['IBB'] = None
                try:
                    row['WP'] = int(row['WP'])
                except (RuntimeError, TypeError, NameError):
                    row['WP'] = None
                try:
                    row['HBP'] = int(row['HBP'])
                except (RuntimeError, TypeError, NameError):
                    row['HBP'] = None
                try:
                    row['BK'] = int(row['BK'])
                except (RuntimeError, TypeError, NameError):
                    row['BK'] = None
                try:
                    row['BFP'] = int(row['BFP'])
                except (RuntimeError, TypeError, NameError):
                    row['BFP'] = None
                try:
                    row['GF'] = int(row['GF'])
                except (RuntimeError, TypeError, NameError):
                    row['GF'] = None
                try:
                    row['R'] = int(row['R'])
                except (RuntimeError, TypeError, NameError):
                    row['R'] = None
                try:
                    row['SH'] = int(row['SH'])
                except (RuntimeError, TypeError, NameError):
                    row['SH'] = None
                try:
                    row['SF'] = int(row['SF'])
                except (RuntimeError, TypeError, NameError):
                    row['SF'] = None
                try:
                    row['GIDP'] = int(row['GIDP'])
                except (RuntimeError, TypeError, NameError):
                    row['GIDP'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO pitchingpost(playerID, yearID, round, teamID, lgID, W, L, G, GS, CG, SHO, SV, "
                        "IPouts, H, ER, HR, BB, SO, BAOpp, ERA, IBB, WP, HBP, BK, BFP, GF, R, SH, SF, "
                        "GIDP) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE pitchingpost a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND "
                    "t.yearID = a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing pitchingpost to MariaDB Platform: {e}")


def import_data_salaries(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('Salaries.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                row['yearID'] = int(row['yearID'])
                try:
                    row['salary'] = float(row['salary'])
                except (RuntimeError, TypeError, NameError):
                    row['salary'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO salaries(yearID, teamID, lgID, playerID, salary) VALUES(%s, %s, %s, %s, %s)", list(data))
        cur.execute("UPDATE salaries a SET a.team_ID = (SELECT ID FROM teams t WHERE t.lgID = a.lgID AND "
                    "t.yearID = a.yearID AND t.teamID = a.teamID)")
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing salaries to MariaDB Platform: {e}")


def import_data_schools(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('Schools.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO schools(schoolID, name_full, city, state, country) VALUES(%s, %s, %s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing schools to MariaDB Platform: {e}")


def import_data_collegeplaying(conn):
    try:
        cur = conn.cursor()
        data = set()
        with open('CollegePlaying.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                row = {key: (value if value != '' else None) for (key, value) in row.items()}
                try:
                    row['yearID'] = int(row['yearID'])
                except (RuntimeError, TypeError, NameError):
                    row['yearID'] = None
                data.add(tuple(row.values()))
        cur.executemany("INSERT INTO collegeplaying(playerID, schoolID, yearID) VALUES(%s, %s, %s)", list(data))
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing collegeplaying to MariaDB Platform: {e}")


def import_data_user(conn):
    try:
        cur = conn.cursor()
        data = set()
        cur.execute("INSERT INTO user(username, password) VALUES('" +
                    csi3335fall2021.mysql['user'] + "', '" +
                    generate_password_hash(csi3335fall2021.mysql['password'])
                    + "');");
        cur.close()
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error importing User to MariaDB Platform: {e}")



if __name__ == '__main__':
    try:
        connection = mysql.connector.connect(
            host=csi3335fall2021.mysql['host'],
            port=csi3335fall2021.mysql['port'],
            user=csi3335fall2021.mysql['user'],
            password=csi3335fall2021.mysql['password'],
            database=csi3335fall2021.mysql['database']
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to MariaDB Platform: {err}")
        sys.exit(1)
    connection.autocommit = False
    import_data_people(connection)
    import_data_awardsmanagers(connection)
    import_data_awardsplayers(connection)
    import_data_awardssharemanagers(connection)
    import_data_awardsshareplayers(connection)
    import_data_teamsfranchises(connection)
    import_data_teams(connection)
    import_data_teamshalf(connection)
    import_data_seriespost(connection)
    import_data_allstarfull(connection)
    import_data_appearances(connection)
    import_data_batting(connection)
    import_data_battingpost(connection)
    import_data_fielding(connection)
    import_data_fieldingof(connection)
    import_data_fieldingofsplit(connection)
    import_data_fieldingpost(connection)
    import_data_halloffame(connection)
    import_data_managers(connection)
    import_data_managershalf(connection)
    import_data_parks(connection)
    import_data_homegames(connection)
    import_data_pitching(connection)
    import_data_pitchingpost(connection)
    import_data_salaries(connection)
    import_data_schools(connection)
    import_data_collegeplaying(connection)
    import_data_user(connection)
    connection.close()
