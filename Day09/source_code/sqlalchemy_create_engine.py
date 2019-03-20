
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from client_models import Base

# wskazanie gdzie tworzymy bazę
engine = create_engine('sqlite:///clients_orm.db')

# utworzenie struktury
Base.metadata.create_all(engine)

# utworzenie obiektu sesji
Session = sessionmaker(bind=engine)
