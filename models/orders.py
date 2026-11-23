from datetime import datetime, timezone
from extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False, default="pending")
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    items = db.relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        db.CheckConstraint(
            "status IN ('pending', 'processing', 'shipped', 'delivered', 'finished')",
            name="check_order_status"
        ),
    )