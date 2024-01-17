# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
