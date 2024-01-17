from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, Date, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Race(Base):
    __tablename__ = "race"
    race_id = Column(Integer(), primary_key=True)
    surface_type = Column(String(10))
    race_date = Column(DateTime())
    track_id = Column(Integer(), ForeignKey("track.track_id"))
    race_class = Column(Integer())
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    track = relationship("Track", uselist=False)


class Track(Base):
    __tablename__ = "track"
    track_id = Column(Integer(), primary_key=True)
    track_state = Column(String(2))
    track_country = Column(String(4))
    track_timezone = Column(String(4))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Horse(Base):
    __tablename__ = "horse"
    horse_id = Column(Integer(), primary_key=True)
    horse_name = Column(String(255))
    horse_birthdate = Column(Date())
    sire = Column(String(255))
    dame = Column(String(255))
    claiming_price = Column(Float())
    sales_price = Column(Float())
    sex = Column(String())
    breed = Column(String())
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class HorsePerformance(Base):
    __tablename__ = "horse_performance"
    performance_id = Column(Integer(), primary_key=True)
    horse_id = Column(Integer(), ForeignKey("horse.horse_id"))
    track_id = Column(Integer(), ForeignKey("track.track_id"))
    race_id = Column(Integer(), ForeignKey("race.race_id"))
    finishing_time = Column(Float())
    finishing_place = Column(Integer())
    pole_position = Column(Integer())
    jockey = Column(Integer(), ForeignKey("jockey.jockey_id"))
    trainer = Column(Integer(), ForeignKey("trainer.trainer_id"))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    horse = relationship("Horse", uselist=False)
    track = relationship("Track", uselist=False)
    race = relationship("Race", uselist=False)


class Jockey(Base):
    __tablename__ = "jockey"
    jockey_id = Column(Integer(), primary_key=True)
    jockey_lname = Column(String(255))
    jockey_fname = Column(String(255))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Trainer(Base):
    __tablename__ = "trainer"
    trainer_id = Column(Integer(), primary_key=True)
    trainer_lname = Column(String(255))
    trainer_fname = Column(String(255))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('sqlite:///:horse_performance.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

