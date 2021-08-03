from sqlalchemy import Column,Integer,VARCHAR,TEXT,Float,ForeignKey,BINARY,DATETIME
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import relationship


BASE: DeclarativeMeta = declarative_base()

class Project(BASE):
    __tablename__= "Project"
    idProject = Column(Integer,primary_key=True,autoincrement=True)
    idNGO = Column(Integer,ForeignKey("NGO.idNGO"))
    idImage = Column(Integer,ForeignKey("Image.idImage"))
    shortDescription = Column(TEXT)
    idSolution = Column(Integer,ForeignKey("Solution.idSolution"))
    idSummary = Column(Integer,ForeignKey("Summary.idSummary"))
    idProblem = Column(Integer,ForeignKey("Problem.idProblem"))
    nameProject = Column(VARCHAR(256))
    statusProject = Column(Integer)
    amountProject = Column(Float)
    shouldAmountProject = Column(Float)
    paymentInformationProject = Column(VARCHAR(256))
    pageProject = Column(VARCHAR(256))
    

    milestone = relationship("Milestone",back_populates="project")

class Milestone(BASE):
    __tablename__ = "Milestone"
    idMilestone = Column(Integer,primary_key=True,autoincrement=True)
    idImage = Column(Integer,ForeignKey("Image.idImage"))
    
    idProject = Column(Integer,ForeignKey("Project.idProject"))

    project = relationship("Project",back_populates="milestone")
    nameMilestone = Column(VARCHAR(256))
    amountMilestone = Column(Float)
    descriptionMilestone = Column(TEXT)

class Image(BASE):
    __tablename__ = "Image"
    idImage = Column(Integer,primary_key=True,autoincrement=True)
    fileImage = Column(VARCHAR(256))
    descriptionImage = Column(TEXT)
    formatImage = Column(VARCHAR(256))

class User(BASE):
    __tablename__ = "User"
    idUser = Column(Integer,primary_key=True,autoincrement=True)
    firstNameUser = Column(VARCHAR(256))
    lastNameUser = Column(VARCHAR(256))
    emailUser = Column(VARCHAR(256))
    passwordtokenUser = Column(VARCHAR(256))
    publickeyUser = Column(VARCHAR(256))
    privatkeyUser = Column(VARCHAR(256))
    registryAtUser = Column(DATETIME)
    balanceUser = Column(Float)

class Payment(BASE):
    __tablename__ = "Payment"
    idPayment = Column(Integer,primary_key=True,autoincrement=True)
    idUser = Column(Integer,ForeignKey("User.idUser"))
    idProject = Column(Integer,ForeignKey("Project.idProject"))
    amountPayment = Column(Float)
    statePayment = Column(VARCHAR(256))
    ## Datetime als Dateiformat statt date im pdm und er
    datePayment = Column(DATETIME)
    
class NGO(BASE):
    __tablename__ = "NGO"
    idNGO = Column(Integer,primary_key=True,autoincrement=True)
    nameNGO = Column(VARCHAR(256))
    emailNGO = Column(VARCHAR(256))

class Solution(BASE):
    __tablename__ = "Solution"
    idSolution = Column(Integer, primary_key=True, autoincrement=True)
    idImage = Column(Integer,ForeignKey("Image.idImage"))
    descriptionSolution= Column(TEXT)

class Summary(BASE):
    __tablename__ = "Summary"
    idSummary = Column(Integer, primary_key=True, autoincrement=True)
    idImage = Column(Integer,ForeignKey("Image.idImage"))
    descriptionSummary= Column(TEXT)

class Problem(BASE):
    __tablename__ = "Problem"
    idProblem = Column(Integer, primary_key=True, autoincrement=True)
    idImage = Column(Integer,ForeignKey("Image.idImage"))
    descriptionProblem= Column(TEXT)
