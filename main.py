from user import User
from post import Post



#from user import User

# initializing a users and passing it the parameters

app_user_one = User("hlstartup@gmail.com", "Haggai", "pwd", "DevOps Engineer")
app_user_two = User("rarora@gmail.com", "Rajat", "pwd", "DevOps EngineerLead")

# calling .get_user_info() method to pull user information
app_user_one.get_user_info()
# calling .change_job_title to change user information and passing th job title name
app_user_one.change_job_title("DevOps_Engineer lll")
# calling .get_user_info()  for user_one to get the updated information
app_user_one.get_user_info()

app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)

new_post.get_post_info()