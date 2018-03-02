from user_signup import Users
from add_comment import AddComment

def DeleteComment:
    def __init__(self):
        self.commenr_id
        self.user
        self.comment_id = AddComment.get_comment_id
        
    def delete_comment(self,user,comment_id):
        "value77" in [x for v in dic.values() for x in v]
        if user in Users.get_user:
            if "moderator" in [temp for user in Users.get_user]:
                del AddComment.delcomment[comment_id]
                return {"Message":"Comment deleted"}
        else:
            return {"Message":"User does not exist"}
