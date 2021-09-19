from .settings import db, db_path
from .user import User

if not db.table_exists('user'):
    db.create_tables([User])

