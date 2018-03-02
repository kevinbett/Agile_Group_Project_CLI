import unittest
from add_comment import AddComment

class AddCommentTestCase(unittest.TestCase):
    def test_add_comment(self):
        add_comment_temp = AddComment()
        response = add_comment_temp.add_comment(1,"This is my comment")
        self.assertEqual(response["Message"],"Comment added successfully")