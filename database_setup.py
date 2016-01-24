__author__ = 'dshao'
import sys

#for mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

#configure class code
from  sqlalchemy.ext.declarative import declarative_base

#for mapper
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


# the declarative_base() callable returns a new base class from which all mapped classes should inherit.
# When the class definition is completed, a new Table and mapper() will have been generated.
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)



###insert at end of file ###
#SQLite connects to file-based databases, using the Python built-in module sqlite3 by default.
#As SQLite connects to local files, the URL format is slightly different.
#For a relative file path, this requires three slashes
engine = create_engine('sqlite:///restaurantmenu.db')
# create the table and tell it to create it in the
# database engine that is passed
Base.metadata.create_all(engine)


