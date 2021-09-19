from .settings import db, db_path
from .member import Member

if not db.table_exists('member'):
    db.create_tables([Member])

