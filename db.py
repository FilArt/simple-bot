from sqlalchemy import create_engine

from secrets import DB_HOST, DB_NAME, DB_PWD, DB_USER

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}")
db_conn = engine.connect()
