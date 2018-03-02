class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    comment = Column(String)