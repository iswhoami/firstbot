import os.path

BASEDIR = os.path.dirname(__file__)

LOG_PATH = os.path.join(BASEDIR, 'logs', 'bot.log')
DB_PATH = os.path.join(BASEDIR, 'db', 'database.db')

PHOTO_PATH = os.path.join(BASEDIR, 'files', 'photo.jpg')
INTERVIEW_PATH = os.path.join(BASEDIR, 'files', 'interview.txt')
PORTFOLIO_PATH = os.path.join(BASEDIR, 'files', 'portfolio.txt')
MY_LINK_PATH = os.path.join(BASEDIR, 'files', 'mylink.txt')

PER_PAGE_ITEMS = 1

admins = [6509528444]