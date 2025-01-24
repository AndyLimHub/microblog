import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app,db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post, 'generate_password_hash': generate_password_hash, 'check_password_hash': check_password_hash, 'User': User}