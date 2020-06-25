from . import SESSION, BASE
from sqlalchemy import Column, Integer


class Pack(BASE):
    __tablename__ = "pack"
    pack_id = Column(Integer, primary_key=True, default=1)

    def __init__(self, pack_id):
        self.pack_id = int(pack_id)


Pack.__table__.create(checkfirst=True)


def get_id():
    return SESSION.query(Pack).all()[0]
    SESSION.close()


def update_id(current_id):
    newid = current_id+1
    SESSION.add(Pack(newid))
    SESSION.commit()
    return newid
