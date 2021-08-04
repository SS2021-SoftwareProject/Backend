import requests
from sqlalchemy import Column,Integer,VARCHAR,TEXT,Float,ForeignKey,BINARY,DATETIME
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import List


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
    statusProject = Column(VARCHAR(256))
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
    idSolution = Column(Integer,primary_key=True,autoincrement=True)
    idImage = Column(Integer,ForeignKey("Image.idImage"))
    descriptionSolution= Column(TEXT)

class Summary(BASE):
    __tablename__ = "Summary"
    idSummary = Column(Integer,primary_key=True,autoincrement=True)
    idImage = Column(Integer,ForeignKey("Image.idImage"))
    descriptionSummary= Column(TEXT)

class Problem(BASE):
    __tablename__ = "Problem"
    idProblem = Column(Integer,primary_key=True,autoincrement=True)
    idImage = Column(Integer,ForeignKey("Image.idImage"))
    descriptionProblem= Column(TEXT)

def add_sample_data(db_session):
    """
    Adds some sample data.
    """

    session = db_session()

    # fictional milestones, sample data

    milestones: List[Milestone] = [
        Milestone(idMilestone=1,
            nameMilestone="Organisation and roles",
            amountMilestone=12,
            descriptionMilestone="Decide who does what and who controls and leads the teams"),
        Milestone(idMilestone=2,
            nameMilestone="Modeling",
            amountMilestone=34,
            descriptionMilestone="Model of the database structure"),
        Milestone(idMilestone=3,
            nameMilestone="Database",
            amountMilestone=45,
            descriptionMilestone="Creation of the database"),
        Milestone(idMilestone=4,
            nameMilestone="API",
            amountMilestone=67,
            descriptionMilestone="Creation of the API for easy access to the database"),
        Milestone(idMilestone=5,
            nameMilestone="GUI",
            amountMilestone=89,
            descriptionMilestone="Visually pleasing GUI to provide access to the API instead of commands"),
    ]

    # fictional images, sample data. fileImage binary points nowhere. Change that if necessary

    images: List[Image] = [
        Image(idImage=1,
            fileImage="https://www.unicef.de/blob/221778/3c89d03bff7e4573ed1e8ab4fbd6d597/drc-mangelernaehrung-plumpy-nut-uni232071-data.jpg",
            descriptionImage="The answer to everything, probably",
            formatImage="jpg"),
        Image(idImage=2,
            fileImage="https://www.worldvision.de/sites/worldvision.de/files/styles/campaign_teaser_896x672/public/editorial/campaign-teaser/2019-12/WolrdVison_Katasprophenhilfe_HungerinAfrika_HeroSpace.jpg?itok=RmGjmU1d",
            descriptionImage="A nice image",
            formatImage="jpg"),
        Image(idImage=3,
            fileImage="https://www.kfw-entwicklungsbank.de/Bilder/Bilderordner/SDGs/SDG-2/SDG_2_Interview_Responsive_1080x608.jpg",
            descriptionImage="Another nice image",
            formatImage="png"),
        Image(idImage=4,
            fileImage="https://unicef.at/fileadmin/_processed_/b/9/csm_UNICEF-kind-leerer-teller-UN0345138_d78780f7b6.jpg",
            descriptionImage="The best image",
            formatImage="png"),
        Image(idImage=5,
            fileImage="https://www.unicef.de/blob/202746/503c5ca7ad1d6448c10da3c805599367/suedsudan-maria-buehne-un0152183-data.jpg",
            descriptionImage="Don't use this image",
            formatImage="jpg"),
    ]

    # fictional user, sample data. Keys generated randomly from hex values. No logic.

    user: List[User] = [
        User(idUser=1,
            firstNameUser="tester",
            lastNameUser="testy",
            emailUser="test@test.com",
            passwordtokenUser="123",
            publickeyUser="0x54DD30d58a423332C64a180D830e264D8C23a8cF",
            privatkeyUser="e7ef6fa199620acaa0c1b04f6bcbbbb6c22e2c52e9685386427f128eae4c8630",
            registryAtUser=datetime(2000, 2, 20),
            balanceUser=42),
        User(idUser=2,
            firstNameUser="Peter",
            lastNameUser="Python",
            emailUser="Peter.Python@example.com",
            passwordtokenUser="1652051816252081514",
            publickeyUser="0x54DD30d58a423332C64a180D830e264D8C23a8cF",
            privatkeyUser="e7ef6fa199620acaa0c1b04f6bcbbbb6c22e2c52e9685386427f128eae4c8630",
            registryAtUser=datetime(2008, 8, 8),
            balanceUser=420),
        User(idUser=3,
            firstNameUser="Juliana",
            lastNameUser="Java",
            emailUser="Juliana.Java@example.com",
            passwordtokenUser="10211291141101221",
            publickeyUser="0x54DD30d58a423332C64a180D830e264D8C23a8cF",
            privatkeyUser="e7ef6fa199620acaa0c1b04f6bcbbbb6c22e2c52e9685386427f128eae4c8630",
            registryAtUser=datetime(1996, 11, 5),
            balanceUser=666),
        User(idUser=4,
            firstNameUser="Christian",
            lastNameUser="Cplusplus",
            emailUser="Christian.Cplusplus@example.com",
            passwordtokenUser="381891920911431612211916122119",
            publickeyUser="0x54DD30d58a423332C64a180D830e264D8C23a8cF",
            privatkeyUser="e7ef6fa199620acaa0c1b04f6bcbbbb6c22e2c52e9685386427f128eae4c8630",
            registryAtUser=datetime(2002, 11, 15),
            balanceUser=1337),
        User(idUser=5,
            firstNameUser="Henrik",
            lastNameUser="Haskell",
            emailUser="Max.Mustermann@example.com",
            passwordtokenUser="85141891181191151212",
            publickeyUser="0x54DD30d58a423332C64a180D830e264D8C23a8cF",
            privatkeyUser="e7ef6fa199620acaa0c1b04f6bcbbbb6c22e2c52e9685386427f128eae4c8630",
            registryAtUser=datetime(2005, 9, 4),
            balanceUser=69),
    ]

    # fictional payment, sample data

    payments: List[Payment] = [
        Payment(idPayment=1,
            amountPayment=69,
            statePayment="completed",
            datePayment=datetime(2020, 3, 7)),
        Payment(idPayment=2,
            amountPayment=420,
            statePayment="completed",
            datePayment=datetime(2019, 4, 18)),
        Payment(idPayment=3,
            amountPayment=1337,
            statePayment="completed",
            datePayment=datetime(2016, 1, 7)),
        Payment(idPayment=4,
            amountPayment=42,
            statePayment="completed",
            datePayment=datetime(2012, 9, 4)),
        Payment(idPayment=5,
            amountPayment=666,
            statePayment="completed",
            datePayment=datetime(2010, 10, 10)),
    ]

    # fictional ngo, sample data

    ngos: List[NGO] = [
        NGO(idNGO=1,
            nameNGO="Example Name",
            emailNGO="example.name@example.com"),
        NGO(idNGO=2,
            nameNGO="Trusted Orginasation",
            emailNGO="trusted.organisation@example.com"),
        NGO(idNGO=3,
            nameNGO="Not A Scam",
            emailNGO="not.a.scam@example.com"),
        NGO(idNGO=4,
            nameNGO="Your standard NGO",
            emailNGO="your.standard.ngo@example.com"),
        NGO(idNGO=5,
            nameNGO="Ran out of ideas",
            emailNGO="ran.out.of.ideas@example.com"),
    ]

    # fictional solution, sample data


    solutions: List[Solution] = [
        Solution(idSolution =1,
                descriptionSolution="One way to solve the problem Nr.1"),
        Solution(idSolution =2,
                descriptionSolution="One way to solve the problem Nr.2"),
        Solution(idSolution =3,
                descriptionSolution="One way to solve the problem Nr.3")
    
    ]

    # set Image to Solution

    solutions[0].idImage = images[0].idImage
    solutions[1].idImage = images[1].idImage
    solutions[2].idImage = images[2].idImage


    # fictional summary, sample data


    summaries: List[Summary] = [
        Summary(idSummary =1,
                descriptionSummary="A summary of the project Nr.1"),
        Summary(idSummary =2,
                descriptionSummary="A summary of the project Nr.2"),
        Summary(idSummary =3,
                descriptionSummary="A summary of the project Nr.3")
    
    ]

    # set Image to Summery

    summaries[0].idImage = images[0].idImage
    summaries[1].idImage = images[1].idImage
    summaries[2].idImage = images[2].idImage


    # fictional problem, sample data


    problems: List[Problem] = [
        Problem(idProblem=1,
                descriptionProblem="A problem from the project Nr.1"),
        Problem(idProblem =2,
                descriptionProblem="A problem from the project Nr.2"),
        Problem(idProblem =3,
                descriptionProblem="A problem from the project Nr.3")
    
    ]

    # set Image to Problem
    
    problems[0].idImage = images[0].idImage
    problems[1].idImage = images[1].idImage
    problems[2].idImage = images[2].idImage


    # fictional project, sample data

    projects: List[Project] = [
        Project(idProject=1,
                nameProject= "Test Project Nr.1",
                statusProject= "in progress",
                shortDescription = "Its short",
                amountProject=500,
                shouldAmountProject= 10000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project1.com"
                ),

        Project(idProject=2,
                nameProject= "Test Project Nr.2",
                statusProject= "finished",
                shortDescription = "Its extremly short",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),

        Project(idProject=3,
                nameProject= "Test Project Nr.3",
                statusProject= "almost finished",
                shortDescription = "The shortest you ve ever seen",
                amountProject=2500,
                shouldAmountProject= 3000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project3.com"
                ),
        Project(idProject=4,
                nameProject= "Test Project Nr.4",
                statusProject= "finished",
                shortDescription = "Its extremly short",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),
        Project(idProject=5,
                nameProject= "Test Project Nr.5",
                statusProject= "finished",
                shortDescription = "Its extremly short",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),
        Project(idProject=6,
                nameProject= "Test Project Nr.6",
                statusProject= "finished",
                shortDescription = "Its extremly short",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),
        Project(idProject=7,
                nameProject= "Test Project Nr.7",
                statusProject= "finished",
                shortDescription = "Its extremly short",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),
        Project(idProject=8,
                nameProject= "Test Project Nr.8",
                statusProject= "finished",
                shortDescription = "Its extremly short",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),
        Project(idProject=9,
                nameProject= "Test Project Nr.9",
                statusProject= "finished",
                shortDescription = "Its extremly short",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),
        Project(idProject=10,
                nameProject= "Test Project Nr.10",
                statusProject= "finished",
                shortDescription = "Its extremly short",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),
        Project(idProject=11,
                nameProject= "Test Project Nr.11",
                statusProject= "finished",
                shortDescription = "Its extremly short",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),
        Project(idProject=12,
                nameProject= "Test Project Nr.12",
                statusProject= "finished",
                shortDescription = "Its extremly short",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                )
    ]

    # foreign key assignments for projects
    projects[0].idNGO =ngos[0].idNGO
    projects[0].idImage = images[0].idImage
    
    projects[1].idImage = images[1].idImage
    projects[1].idNGO =ngos[1].idNGO

    projects[2].idImage = images[2].idImage
    projects[2].idNGO =ngos[2].idNGO

    projects[3].idImage = images[3].idImage
    projects[3].idNGO =ngos[2].idNGO

    projects[4].idImage = images[4].idImage
    projects[4].idNGO =ngos[2].idNGO

    projects[5].idImage = images[2].idImage
    projects[5].idNGO =ngos[2].idNGO

    projects[6].idImage = images[1].idImage
    projects[6].idNGO =ngos[2].idNGO

    projects[7].idImage = images[3].idImage
    projects[7].idNGO =ngos[2].idNGO

    projects[8].idImage = images[4].idImage
    projects[8].idNGO =ngos[2].idNGO

    projects[9].idImage = images[1].idImage
    projects[9].idNGO =ngos[2].idNGO

    projects[10].idImage = images[2].idImage
    projects[10].idNGO =ngos[2].idNGO

    projects[11].idImage = images[1].idImage
    projects[11].idNGO =ngos[2].idNGO


    

    # relationship sample assignments
    

    milestones[0].project = projects[0]
    milestones[1].project = projects[0]
    milestones[2].project = projects[1]
    milestones[3].project = projects[1]
    milestones[4].project = projects[2]
  
    # foreign key assignments

    milestones[0].idImage = images[0].idImage
    milestones[1].idImage = images[1].idImage
    milestones[2].idImage = images[2].idImage
    milestones[3].idImage = images[3].idImage
    milestones[4].idImage = images[4].idImage
    
    milestones[0].idProject = projects[0].idProject
    milestones[1].idProject = projects[0].idProject
    milestones[2].idProject = projects[1].idProject
    milestones[3].idProject = projects[1].idProject
    milestones[4].idProject = projects[2].idProject

    '''
    payments[0].idUser = user[0].idUser
    payments[1].idUser = user[1].idUser
    payments[2].idUser = user[2].idUser
    #payments[3].idUser = user[3].idUser
    #payments[4].idUser = user[4].idUser
    

    payments[0].idProject = projects[0].idProject
    payments[1].idProject = projects[1].idProject
    payments[2].idProject = projects[2].idProject
    payments[3].idProject = projects[2].idProject
    payments[4].idProject = projects[2].idProject
    '''


    object = [*ngos, *images, *solutions, *summaries, *problems, *projects, *user, *payments]
   

    for obj in object:
        session.add(obj)
    
    
   

    
    session.commit()
