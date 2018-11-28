import unittest
from app.models import Review

class TestComment(unittest.TestCase):
    """
    This class  will test the comments
    """

    def setUp(self):
        """
        This will create a new comment before each test
        """
        self.new_comment = Comment(title = "Nice")

    def tearDown(self):
        """
        THis will clear the db after each test
        """
        Comment.query.delete()

    def test_is_instance(self):
        """
        This will test whether the comment created is an instance of the Comment class
        """
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_init(self):
        """
        This willl test whether the new_comment is instantiated correctly
        """
        self.assertTrue(self.new_comment.title == "Nice")

    def test_save_review(self):
        """
        This will test whether the comment is added to the db
        """
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)
    
