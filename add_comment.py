from user_signup import Users

class AddComment:
    def __init__(self):
        self.comment = {}
        # self.comment_body = comment_body
        # self.comment_id = comment_id
    def add_comment(self,comment_id,comment_body):
        self.comment[comment_id] = comment_body
        return {"Message":"Comment added successfully"}
    def get_comment_id(self):
        self.comment[comment_id] = newcomment
        return newcomment
