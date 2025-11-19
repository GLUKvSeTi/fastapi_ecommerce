from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    rating_id = Column(Integer, ForeignKey('ratings.id'), nullable=False)
    comment = Column(String)
    comment_date = Column(String)
    is_active = Column(Boolean, default=True)

    rating = relationship('Rating', back_populates='reviews')
    product = relationship('Product', back_populates='reviews')
    user = relationship('User', back_populates='reviews')