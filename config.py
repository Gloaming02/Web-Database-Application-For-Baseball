import os
import csi3335fall2021


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'KHz'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://' + csi3335fall2021.mysql['user'] + ':' + csi3335fall2021.mysql['password'] + '@' + \
                              csi3335fall2021.mysql['host'] + ':' + str(csi3335fall2021.mysql['port']) + '/' + \
                              csi3335fall2021.mysql['database']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
