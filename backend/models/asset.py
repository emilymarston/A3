from .db import db
from datetime import datetime

class Asset(db.Model):
    __tablename__ = 'assets'

    id              = db.Column(db.Integer, primary_key=True)
    total_table     = db.Column(db.Integer, nullable=False)
    total_chair     = db.Column(db.Integer, nullable=False)
    is_available    = db.Column(db.Boolean, default=True)

    def __init__(self, total_table, total_chair):
        self.total_table = total_table
        self.total_chair = total_chair

    def is_available(self, required_tables):
        return self.total_table >= required_tables