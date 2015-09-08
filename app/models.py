from app import db

class AmazonIN(db.Model):
    """Stores all the products from amazon.in"""

    product_id = db.Column(db.String(30), primary_key=True)
    url = db.Column(db.String(256), nullable=False)
    sentiment_score = db.Column(db.Numeric(3, 2), nullable=False)
    sentiment = db.Column(db.String(8), nullable=False)
    added_on = db.Column(db.DateTime, nullable=False)
    modified_on = db.Column(db.DateTime, nullable=False)
