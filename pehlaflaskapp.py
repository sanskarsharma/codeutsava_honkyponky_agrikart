from app import app_instance, db_instance
# here 1st app is our package and 2nd is our application instance
from app.models import User, Post

@app_instance.shell_context_processor
def making_our_shell_context():
    return { "db": db_instance, "User": User, "Post": Post }
