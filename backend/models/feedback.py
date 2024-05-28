from . import db

class Feedback(db.model):
    __tablename__ = 'feedback'

    feedback_id     = db.Column(db.Integer)
    customer_id     = db.Column(db.Integer)
    content         = db.Column(db.String(100))
    rating          = db.Column(db.Integer)

    @staticmethod
    def submit_feedback(customer_id, content, rating):
        new_feedback = Feedback(customer_id=customer_id, content=content, rating=rating)
        db.session.add(new_feedback)
        db.session.commit()