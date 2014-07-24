#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Sequence, String, Float, Boolean
from base import Base, Entity

class TripStartTime(Base, Entity):
  __tablename__ = 'trips_start_times'
  trip_id = Column(String(50), primary_key=True)
  service_id = Column(String(50))
  start_time = Column(String(50))