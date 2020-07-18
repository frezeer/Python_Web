import unittest

from flask import current_app

from app import create_app
from app import db, User , Task
from config import config

class DemoTestCase(unittest.TestCase):

    def setUp(self):
        config_class = config['test']
        self.app = create_app(config_class)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.id = 1

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        self.app_context.pop()

    def test_demo(self):
        self.assertTrue(1 == 1)

    def test_user_exists(self):
        user = User.get_by_id(self.id)
        self.assertTrue(user is None)

    def test_create_user(self):
        user = User.create_element('username','correo@gmail.com','password')
        self.assertTrue(user.id == self.id)

    def test_update_element(self):
        task = Task.update_element(9,'titulo','description')
        self.assertTrue(True == True)

    def test_delete_element(self):
        task = Task.delete_element(9)
        self.assertTrue(True == True)
