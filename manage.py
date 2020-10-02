from app import create_app, db
from app.model import User,Schools,Course,Exam,Answer
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand


app = create_app('development')

migrate = Migrate(app, db)

manager =  Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Course = Course,  Exam = Exam, Answer = Answer )

manager.add_command('server', Server)
@manager.command
def test():
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)


if __name__ == '__main__':
    manager.run()

from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
from app.model import User

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('serve', Server)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    manager.run()