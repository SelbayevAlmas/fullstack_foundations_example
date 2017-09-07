from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base,Restaurant,MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


one= Restaurant(name = "Pizza Palace")
session.add(one)
two= Restaurant(name = "Taksim")
session.add(two)
three= Restaurant(name = "Iftar")
session.add(three)
four= Restaurant(name = "McDonalds")
session.add(four)
five= Restaurant(name = "Burger King")
session.add(five)

session.commit()


listOfRes = session.query(Restaurant).all()
res = session.query(Restaurant).first()
for item in listOfRes:
    print(str(item.id)+" "+item.name)

