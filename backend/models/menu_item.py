from .db import db

class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    menu_item_id        = db.Column(db.Integer, primary_key=True)
    menu_description    = db.Column(db.String(255), nullable=False)
    price               = db.Column(db.Float, nullable=False)

    def __init__(self, menu_description, price):
        self.menu_description = menu_description
        self.price = price

    def to_dict(self):
        return {
            "menu_item_id": self.menu_item_id,
            "menu_description": self.menu_description,
            "price": self.price
        }

    def get_menu_item_id(self):
        return self.menu_item_id

    def get_menu_item_description(self):
        return self.menu_description

    def get_menu_item_price(self):
        return self.price
