from user_signup import Users

class AddComment:
    def __init__(self):
        self.comment = {}
        self.user = user
        self.comment_body = comment_body
    def add_comment(self,comment_id,user,comment_body):
        self.comment[comment_id] = user
        self.comment[comment_id].append(user)
        self.comment[comment_id].append(comment_body)
        return {"Message":"Comment created successfully"}
    def get_comment_id(self):
        self.comment[comment_id] = newcomment
        return newcomment
