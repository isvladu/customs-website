from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String

from .entity import Base, Entity


class Match(Entity, Base):
    __tablename__ = "matches"

    match_id = Column(Integer)
    player_0 = Column(String)
    player_1 = Column(String)
    player_2 = Column(String)
    player_3 = Column(String)
    player_4 = Column(String)
    player_5 = Column(String)
    player_6 = Column(String)
    player_7 = Column(String)
    player_8 = Column(String)
    player_9 = Column(String)

    def __init__(
        self,
        match_id,
        player_0,
        player_1,
        player_2,
        player_3,
        player_4,
        player_5,
        player_6,
        player_7,
        player_8,
        player_9,
        created_by,
    ):
        Entity.__init__(self, created_by)
        self.match_id = match_id
        self.player_0 = player_0
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_3 = player_3
        self.player_4 = player_4
        self.player_5 = player_5
        self.player_6 = player_6
        self.player_7 = player_7
        self.player_8 = player_8
        self.player_9 = player_9


class MatchSchema(Schema):
    id = fields.Number()
    match_id = fields.Number()
    player_0 = fields.Str()
    player_1 = fields.Str()
    player_2 = fields.Str()
    player_3 = fields.Str()
    player_4 = fields.Str()
    player_5 = fields.Str()
    player_6 = fields.Str()
    player_7 = fields.Str()
    player_8 = fields.Str()
    player_9 = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
