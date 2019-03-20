
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from goods_models import Base

engine = create_engine('sqlite:///goods_orm.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
