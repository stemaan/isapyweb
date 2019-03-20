from create_db_create_engine import Session

from goods_models import Goods

session = Session()

fruit = Goods(name='Apple', price=4, origin='Poland')
session.add(fruit)

fruit = Goods(name='Banana', price=8, origin='Brasil')
session.add(fruit)

fruit = Goods(name='Plum', price=6, origin='Poland')
session.add(fruit)

fruit = Goods(name='Raspberry', price=6, origin = 'Spain')
session.add(fruit)

fruit = Goods(name='Blueberry', price=5, origin = 'Poland')
session.add(fruit)

session.commit()
