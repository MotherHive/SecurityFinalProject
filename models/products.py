class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    order_items = db.relationship("OrderItem", back_populates="product")

    __table_args__ = (
        db.CheckConstraint("price >= 0", name="check_product_price_non_negative"),
    )