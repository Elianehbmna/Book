import unittest
from app.models import Pitch, User, Comment
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(description = "funny right", category='Comedy')
        self.new_comment = Comment(description = "hahah", pitch=self.new_pitch)
    
    def tearDown(self):
        db.session.delete(self)
        User.query.commit()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.description,"hahah")
        self.assertEquals(self.new_comment.pitch,self.new_pitch, 'funny right')