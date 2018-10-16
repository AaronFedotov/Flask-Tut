#! /usr/bin/env python

from thermos import app, db
from thermos.models import User, Bookmark, Tag
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def initdb():
	db.create_all()
	db.session.add(User(username='aaron', email='aaron@example.com', password='aaronpassword'))
	db.session.add(User(username='oleg', email='oleg@example.com', password='olegpassword'))
	db.session.commit()
	print('Initialized the database')


@manager.command
def insert_data():
	#db.create_all()
	aaron = User(username="aaron", email="aaron@example.com", password="aaronpassword")
	db.session.add(aaron)

	def add_bookmark(url, description, tags):
		db.session.add(Bookmark(url=url, description=description, user=aaron, tags=tags))

	for name in ['python', 'questions', 'programming', 'training', 'news', 'orm', 'data']:
		db.session.add(Tag(name=name))
	db.session.commit()

	add_bookmark('http://www.pluralsight.com', 'Pluralsight. Hardcore developer training.', 'training, programming')
	add_bookmark('http://www.python.org', 'Python - my favorite language', 'python')
	add_bookmark('http://www.reddit.com', 'Reddit. Frontpage of the internet', 'news')
	add_bookmark('http://www.sqlalchemy.org', 'Nice ORM framework', 'orm')
	add_bookmark('http://www.ipython.org', 'IPython. Interactive computing', 'data')
	add_bookmark('http://www.stackoverflow.com', 'For all your programmng questions', 'questions')

	oleg = User(username='oleg', email='oleg@example.ru', password='olegpassword')
	db.session.add(oleg)
	db.session.commit()

@manager.command
def dropdb():
	if prompt_bool("Are you sure you want to lose all your data?"):
		db.drop_all()
		print('Dropped the database')

if __name__ == '__main__':
	manager.run()