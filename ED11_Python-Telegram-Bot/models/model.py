from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('sqlite:///bot.db', future=True)
Base = declarative_base()


class Bot_db(Base):
    __tablename__ = "Bot_db"
    id = Column(Integer, unique=True, primary_key=True)
    user_id = Column(Integer, unique=False, nullable=False)
    message = Column(String)

    def __repr__(self):
         return f"Bot_db(id={self.id!r}, name={self.name!r}, product_id={self.product_id!r})"
    
    def add_user(userid, message):
        session = Session(engine)
        Add_date = Bot_db(
            user_id=userid,
            message=message,
        )
        session.add_all([Add_date])
        session.commit()