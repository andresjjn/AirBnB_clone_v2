#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import *
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from sqlalchemy import MetaData
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """Getter of reviews"""
        from models import storage
        list_reviews = []
        for review in storage.all(Review):
            if self.id is review.place_id:
                list_reviews.append(review)
        return list_reviews

    @property
    def amenities(self):
        """Getter of amenities"""
        from models import storage
        list_amenities = []
        for amenity in storage.all(Amenity).values():
            if amenity.id == self.amenity_ids:
                list_amenities.append(amenity)
        return list_amenities

    @amenities.setter
    def amenities(self, amenity):
        """Setter of amenities"""
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity)
