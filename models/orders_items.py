from extensions import db

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    order = db.relationship("Order", back_populates="items")

    __table_args__ = (
        db.CheckConstraint("quantity > 0", name="check_item_quantity_positive"),
    )