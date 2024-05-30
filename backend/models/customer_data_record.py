from .db import db
from dataclasses import dataclass, field
from typing import List
from .membership import Membership
from .feedback import Feedback

@dataclass
class CustomerDataRecord:
    membershipsRecord: List[Membership] = field(default_factory=list)
    feedbackRecord: List[Feedback] = field(default_factory=list)

    def addFeedback(self, feedback: Feedback) -> None:
        self.feedbackRecord.append(feedback)
        db.session.add(feedback)
        db.session.commit()

    def addMembership(self, membership: Membership) -> None:
        self.membershipsRecord.append(membership)
        db.session.add(membership)
        db.session.commit()

    def addCustomer(self, customer) -> None:
        # Assuming `customer` is an instance of a Customer model that needs to be added to the database
        db.session.add(customer)
        db.session.commit()
