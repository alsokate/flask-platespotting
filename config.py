import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'a-key'

DEBUG = True
TESTING = False
DATABASE_URI = 'postgres://fcrgvjtgrhdbru:1GGFH4zdj3j0A1qxeK5Vdabv9i@ec2-54-235-194-252.compute-1.amazonaws.com:5432/das4ugkl3ip6g5'