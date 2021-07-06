from sqlalchemy import Column,Integer,VARCHAR,TEXT,Float,ForeignKey,BINARY
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import relationship

BASE: DeclarativeMeta = declarative_base()

class Project(BASE):
    __tablename__= "Project"
    idProject = Column(Integer,primary_key=True,autoincrement=True)
    idNGO = Column(Integer,ForeignKey("NGO.idNGO"))
    ## Was bedeutet diese Zeile?
    nGO = relationship("NGO",back_populates="project")
    idImage = Column(Integer,ForeignKey("Image.idImage"))
    ## Was bedeutet diese Zeile?
    image = relationship("Image",back_populates="project")
    nameProject = Column(VARCHAR(256))
    descriptionProject = Column(TEXT)
    statusProject = Column(Integer)
    amountProject = Column(Float)
    shouldAmountProject = Column(Float)
    paymentInformationProject = Column(VARCHAR(256))
    pageProject = Column(VARCHAR(256))
    shortdescriptionProject = Column(TEXT)

    ## Was bedeutet diese Zeile?
    milestone = relationship("Meilenstein",back_populates="project")

class Milestone(BASE):
    __tablename__ = "Milestone"
    idMilestone = Column(Integer,primary_key=True,autoincrement=True)
    idImage = Column(Integer,ForeignKey("Image.idImage"))
    ## Was bedeutet diese Zeile?
    image = relationship("Image",back_populates="milestone")
    idProject = Column(Integer,ForeignKey("Project.idProject"))
    ## Was bedeutet diese Zeile?
    project = relationshipt("Project",back_populates="project")
    nameMilestone = Column(VARCHAR(256))
    amountMilestone = Column(Float)
    descriptionMilestone = Column(TEXT)

class Image(BASE):
    __tablename__ = "Image"
    idImage = Column(Integer,primary_key=True,autoincrement=True)
    fileImage = Column(BINARY)
    descriptionImage = Column(TEXT)
    formatImage = Column(VARCHAR(256))

class User(BASE):
    __tablename__ = "User"
    