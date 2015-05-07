#!flask/bin/python

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

v = api.db_version(SQLALCHEMY_DATABADE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABADE_URI, SQLALCHEMY_MIGRATE_REPO, v-1)
v = api.db_version(SQLALCHEMY_DATABADE_URI, SQLALCHEMY_MIGRATE_REPO)
print('current database version' + str(v))
