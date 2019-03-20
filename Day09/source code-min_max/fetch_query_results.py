if __name__ == '__main__':
    from goods_models import Goods
    from create_db_create_engine import Session
    from sqlalchemy.sql import func

    session = Session()

    max_val = session.query(func.max(Goods.price)).one()
    print('Max price:', max_val[0])

    min_val = session.query(func.min(Goods.price)).one()
    print('Min price:', min_val[0])

    max_val_from_Poland = session.query(func.max(Goods.price)).filter(Goods.origin == 'Poland').one()
    print('Max price:', max_val_from_Poland[0])

    min_val_from_Poland = session.query(func.min(Goods.price)).filter(Goods.origin == 'Poland').one()
    print('Min price:', min_val_from_Poland[0])
