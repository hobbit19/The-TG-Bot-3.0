from . import SESSION, BASE
from sqlalchemy import Column, Integer


class Pack(BASE):
    __tablename__ = "pack"
    id = Column(Integer, primary_key=True, default=1)

    def __init__(self, id):
        self.id = int(id)


Pack.__table__.create(checkfirst=True)


def get_id():
    return SESSION.query(Pack).get(int(id))
    SESSION.close()


def update_id(current_id):
    newid = current_id+1
    SESSION.add(Pack(newid))
    SESSION.commit()
    return newid
