# manage.py
import sys, os

from flask.ext.script import Manager
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tumblelog import app

manager = Manager(app)

@manager.command
def sayHello():
    print "hello worldddd"
    
@manager.command    
def sayBye():
    print "bye worlddddddd";    
    

if __name__ == "__main__":
    manager.run()
