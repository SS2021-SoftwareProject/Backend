import requests
from sqlalchemy import Column,Integer,VARCHAR,TEXT,Float,ForeignKey,BINARY,DATETIME
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import List
import random


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
            nameMilestone="Hunger relief for the families of Mduku",
            amountMilestone=12,
            descriptionMilestone="Each parcel of food costs $35 and we will distribute one parcel (feeding a family of four) to 72 families who are identified as the most in-need by the tribal authorities and community health teams. "),
        Milestone(idMilestone=2,
            nameMilestone="Hunger relief for the Green Mambas",
            amountMilestone=34,
            descriptionMilestone="The Green Mambas are a group of 14 women, mostly single-mothers, who work seasonally for Wild Tomorrow Fund, helping on our reserve with green jobs including alien plant removal. We want to ensure these strong women and their children do not go hungry each month.  We will deliver 14 food parcels which cost $35 each to each Green Mamba for her family. "),
        Milestone(idMilestone=3,
            nameMilestone="Hunger Relief for the Habanathi Orphans",
            amountMilestone=45,
            descriptionMilestone="These are the most vulnerable children in the community neighboring our wildlife reserve. Most live with their extended families after being orphaned, usually sadly due to HIV.  We will work together with Pastor Bonga of Habanathi EC Charity (who supports the orphans and their caretakers) to purchase food for 15 families. Each food parcel costs $35."),
        Milestone(idMilestone=4,
            nameMilestone="Install a water storage tank and stand.",
            amountMilestone=67,
            descriptionMilestone="Install a water storage tank and stand."),
        Milestone(idMilestone=5,
            nameMilestone="World Peace",
            amountMilestone=89,
            descriptionMilestone="We did it!"),
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
            publickeyUser="0xEFc80dD88d34DdaeAa4dF3E5c2feE45b08e7F19CEB",
            privatkeyUser="0x8DA75ea6aBb332c0e1FF0b67DBCfD3cfCEfaF975Cf",
            registryAtUser=datetime(2000, 2, 20),
            balanceUser=42),
        User(idUser=2,
            firstNameUser="Peter",
            lastNameUser="Python",
            emailUser="Peter.Python@example.com",
            passwordtokenUser="1652051816252081514",
            publickeyUser="0x94bC0bDcaDB2c6FCABdc8F6C448BeBAf77dec0147A",
            privatkeyUser="0x17AF21Ed5D93eaDAa39E2b831FDCcbcc4e0dDCDc9d",
            registryAtUser=datetime(2008, 8, 8),
            balanceUser=420),
        User(idUser=3,
            firstNameUser="Juliana",
            lastNameUser="Java",
            emailUser="Juliana.Java@example.com",
            passwordtokenUser="10211291141101221",
            publickeyUser="0xEaA6334C62ad3AB31aCA929A4AAf58A8eF374496FF",
            privatkeyUser="0xc67b269FAC37b74CBfeaEcae5F06aCd0F8f8eBa754",
            registryAtUser=datetime(1996, 11, 5),
            balanceUser=666),
        User(idUser=4,
            firstNameUser="Christian",
            lastNameUser="Cplusplus",
            emailUser="Christian.Cplusplus@example.com",
            passwordtokenUser="381891920911431612211916122119",
            publickeyUser="0x1813FDa8401259FCBaF4fbE435685Ef553ba86747D",
            privatkeyUser="0xb750f4D1721AFcf4CDc4dCdD349C8a70DD4ffdfc7f",
            registryAtUser=datetime(2002, 11, 15),
            balanceUser=1337),
        User(idUser=5,
            firstNameUser="Henrik",
            lastNameUser="Haskell",
            emailUser="Max.Mustermann@example.com",
            passwordtokenUser="85141891181191151212",
            publickeyUser="0xf05e166Efb85AA602c8AFcDf2E8A7f0B0cDc81a42a",
            privatkeyUser="0xFA2A0E0E7291FfC47d85EC5Ba097dae6BFa152d9EA",
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
                descriptionSolution="As part of Wild Tomorrow Fund’s Community Support program, we quickly sprang into action to organize an emergency hunger relief program. We raised enough funds for our first delivery in May for 63 families in need. Our goal is to raise additional funds to provide at least 100 families with emergency food parcels each month. These parcels will contain essentials such as rice, vegetables, oil, and canned fish and will keep families fed for a month. We are working directly with the community's traditional leadership (the Nduna) to help identify the neediest families. Any funds raised above our goal will enable us to extend the reach of the program. Each parcel included a note from Wild Tomorrow fund with a Zulu saying 'Umuntu ngumuntu ngabuntu' which translates to 'A person is a person because of people', a message of solidarity and our shared humanity in this difficult time. "),
        Solution(idSolution =2,
                descriptionSolution="ChildVoice has solidified plans to expand its presence in the camp, and recently received a grant to build a new Youth Empowerment Center. For ChildVoice's students living in the Malkohi IDP camp – many of whom are victims of Boko Haram and other violent insurgent groups – water is a vital component of the programs they have developed to help war-affected youth recover from trauma and overwhelming loss. Without reliable access to water, ChildVoice simply will not be able to run their agriculture, culinary, and other water-dependent skills training programs.  As a crucial part of their new Youth Empowerment Center in the IDP camp, a new water well -- consisting of a borehole, solar-powered pump, storage tank, and taps -- will address a fundamental rehabilitative and economic development need that will otherwise go unmet. Water is essential for ChildVoice to provide life-changing agricultural and other vocational training programs for hundreds of their students. "),
        Solution(idSolution =3,
                descriptionSolution="South American Initiative will continue providing meals and clean drinking water to children and adults who are suffering from malnutrition in hospitals. New and expecting mothers will receive all the help they need to take care of their babies. We provide things like diapers, formula, feeding bottles, and other supplies with your donations. Help mothers and children survive the Venezuela crisis.")
    
    ]

    # set Image to Solution

    solutions[0].idImage = images[0].idImage
    solutions[1].idImage = images[1].idImage
    solutions[2].idImage = images[2].idImage


    # fictional summary, sample data


    summaries: List[Summary] = [
        Summary(idSummary =1,
                descriptionSummary="The COVID19 crisis has deeply impacted southern Africa and particularly rural communities dependent on wildlife tourism for their livelihoods. Already vulnerable communities are now sliding into deeper poverty and hunger. You can help to provide food parcels to ensure that 100 families in the community next to our wildlife reserve, are able to eat for the month of October as part of our ongoing Hunger Relief Campaign. Just $35 is all it takes to buy a big parcel of food for a family for a month. Your support also keeps wildlife safe, by ensuring hungry people do not have to resort to bushmeat poaching to keep their families fed. "),
        Summary(idSummary =2,
                descriptionSummary="The Malkohi internally displaced persons (IDP) camp in Adamawa State, Nigeria, currently has just one hand-pump water borehole (well and hand pump). It serves a population of 2,000-plus IDPs, most of whom are children and adolescents. ChildVoice is building a new Youth Empowerment Center to provide rehabilitative and skills training services for up to 200 ChildVoice students living in the camp. But this one existing well is simply not sufficient to meet the needs a skills training facility. To meet those needs, ChildVoice seeks to raise $5,600 to drill a new water well for its new Youth Empowerment Center."),
        Summary(idSummary =3,
                descriptionSummary="The health care system in Venezuela is declining rapidly. Each day, the press denounces the failing state of public hospitals. Increasingly, the health care crisis, and the shortage of medicine and food, have plagued the country. The Rafael Malpica hospital, located in Guacara (Valencia, Venezuela) is providing only rice for their patients. Many other hospitals are facing the same situation. Proteins are never included in their diet. This project will feed vulnerable adults and children in different hospitals.")
    
    ]

    # set Image to Summery

    summaries[0].idImage = images[0].idImage
    summaries[1].idImage = images[1].idImage
    summaries[2].idImage = images[2].idImage


    # fictional problem, sample data


    problems: List[Problem] = [
        Problem(idProblem=1,
                descriptionProblem="The COVID19 crisis has deeply impacted the vulnerable communities we work with who live next door to our two wildlife reserves in KwaZulu-Natal South Africa. The economic impacts of South Africa’s strict lockdown are being felt on the ground in our rural community, posing a threat to both people and the protection of wildlife. Many people have lost their jobs and incomes, driving already poor families into deeper poverty and hunger. Community members who were working away from home in the city have returned for the lock-down, putting more pressure on families and their resources. Children in particular are at risk as many depend on a daily meal from school, which has been closed."),
        Problem(idProblem =2,
                descriptionProblem="ChildVoice has been providing counseling, skills training, and related services to traumatized adolescent girls and their children in Nigeria for three years now. The organization is now on the verge of solidifying their presence in the Malkohi IDP camp with a new Youth Empowerment Center, making their students’ dreams of having expanded agricultural and other vocational training programs a reality.  While this is an amazing development, the fact is without a reliable water source to supply the new center, these enhanced programs will simply remain dreams.  A reliable water well is a critical part of the new Youth Empowerment Center. Last year, the camp’s only borehole pump failed -- a life-threatening problem in a country where the temperatures can exceed 100 degrees Fahrenheit during the dry season. The NGO responsible for its installation was unable to effect repairs due to the COVID-19 pandemic. Residents became increasingly desperate for this single source of fresh water to be restored. Because ChildVoice continued to maintain a presence in the camp during the pandemic, it handled the repairs.   But as ChildVoice began planning the construction of a new training center, a stark reality quickly became clear: the camp’s single hand-pump well simply can’t produce enough water to meet the needs of their expanded agriculture program and other vocational programs that require water.  The agriculture program is especially important given ongoing hunger issues in the camp and beyond. One of the most important features of the program that requires a reliable water source will be drip irrigation, which will allow ChildVoice to teach dry season farming. Demonstration plots will also rely heavily on water. Because water is essential for these agriculture programs to be successful, it’s no understatement that for ChildVoice's students living in the IDP camp, water is life. "),
        Problem(idProblem =3,
                descriptionProblem="What is the challenge? According to FAO, in the Global Report on Food Crisis 2017, the worsening economic situation in Venezuela has caused a severe shortage of food and medicine. Many refer to this as the ‘Maduro diet.’ Medical supplies are not being imported to Venezuela. This serious crisis is causing malnutrition, which is far from being alleviated. Hospitals in Venezuela are not providing enough meals for all their patients. Some are only providing rice as their main meal. Most of the patients get thinner day-by-day. It seems that they get sicker during their stay at the hospital due to the lack of protein. A well-balanced meal and proper medication are required for a successful recovery. This, far too often, is not happening.")
    
    ]

    # set Image to Problem
    
    problems[0].idImage = images[0].idImage
    problems[1].idImage = images[1].idImage
    problems[2].idImage = images[2].idImage


    # fictional project, sample data

    projects: List[Project] = [
        Project(idProject=1,
                nameProject= "Meals and Medicine for Venezuelan Hospitals",
                statusProject= "In Progress",
                shortDescription = "Providing new mothers and vulnerable patients in Venezuela with the nutrition, services, and medicine they deserve.",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 1000,
                paymentInformationProject="0xd6F1e5fa1ac59F54F347D84198006Cc923f3750E",
                pageProject= "www.Project1.com"
                ),

        Project(idProject=2,
                nameProject= "Emergency Hunger Relief in South Africa",
                statusProject= "finished",
                shortDescription = "Ensuring vulnerable families in rural South Africa keep food on the table during the COVID19 crisis..",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 800,
                paymentInformationProject="0xd6F1e5fa1ac59F54F347D84198006Cc923f3750E",
                pageProject= "www.Project2.com"
                ),

        Project(idProject=3,
                nameProject= "Fresh Water for Children Displaced by Boko Haram in Nigeria",
                statusProject= "In Progress",
                shortDescription = "Provide water for up to 200 ChildVoice students living in Nigeria’s Malkohi Internally Displaced Persons (IDP) camp",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 3000,
                paymentInformationProject="0xd6F1e5fa1ac59F54F347D84198006Cc923f3750E",
                pageProject= "www.Project3.com"
                ),
        Project(idProject=4,
                nameProject= "Meals and Medicine for Venezuelan Hospitals",
                statusProject= "In Progress",
                shortDescription = "Providing new mothers and vulnerable patients in Venezuela with the nutrition, services, and medicine they deserve.",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 1000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project1.com"
                ),

        Project(idProject=5,
                nameProject= "Emergency Hunger Relief in South Africa",
                statusProject= "finished",
                shortDescription = "Ensuring vulnerable families in rural South Africa keep food on the table during the COVID19 crisis..",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),

        Project(idProject=6,
                nameProject= "Fresh Water for Children Displaced by Boko Haram in Nigeria",
                statusProject= "In Progress",
                shortDescription = "Provide water for up to 200 ChildVoice students living in Nigeria’s Malkohi Internally Displaced Persons (IDP) camp",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 5432,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project3.com"
                ),
        Project(idProject=7,
                nameProject= "Meals and Medicine for Venezuelan Hospitals",
                statusProject= "In Progress",
                shortDescription = "Providing new mothers and vulnerable patients in Venezuela with the nutrition, services, and medicine they deserve.",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 10000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project1.com"
                ),

        Project(idProject=8,
                nameProject= "Emergency Hunger Relief in South Africa",
                statusProject= "finished",
                shortDescription = "Ensuring vulnerable families in rural South Africa keep food on the table during the COVID19 crisis..",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 1234,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),

        Project(idProject=9,
                nameProject= "Fresh Water for Children Displaced by Boko Haram in Nigeria",
                statusProject= "In Progress",
                shortDescription = "Provide water for up to 200 ChildVoice students living in Nigeria’s Malkohi Internally Displaced Persons (IDP) camp",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 3210,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project3.com"
                ),
        Project(idProject=10,
                nameProject= "Meals and Medicine for Venezuelan Hospitals",
                statusProject= "In Progress",
                shortDescription = "Providing new mothers and vulnerable patients in Venezuela with the nutrition, services, and medicine they deserve.",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 1560,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project1.com"
                ),

        Project(idProject=11,
                nameProject= "Emergency Hunger Relief in South Africa",
                statusProject= "finished",
                shortDescription = "Ensuring vulnerable families in rural South Africa keep food on the table during the COVID19 crisis..",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),

        Project(idProject=12,
                nameProject= "Fresh Water for Children Displaced by Boko Haram in Nigeria",
                statusProject= "In Progress",
                shortDescription = "Provide water for up to 200 ChildVoice students living in Nigeria’s Malkohi Internally Displaced Persons (IDP) camp",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 12000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project3.com"
                ),
        Project(idProject=13,
                nameProject= "Meals and Medicine for Venezuelan Hospitals",
                statusProject= "In Progress",
                shortDescription = "Providing new mothers and vulnerable patients in Venezuela with the nutrition, services, and medicine they deserve.",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 10000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project1.com"
                ),

        Project(idProject=14,
                nameProject= "Emergency Hunger Relief in South Africa",
                statusProject= "finished",
                shortDescription = "Ensuring vulnerable families in rural South Africa keep food on the table during the COVID19 crisis..",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 500,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),

        Project(idProject=15,
                nameProject= "Fresh Water for Children Displaced by Boko Haram in Nigeria",
                statusProject= "In Progress",
                shortDescription = "Provide water for up to 200 ChildVoice students living in Nigeria’s Malkohi Internally Displaced Persons (IDP) camp",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 3000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project3.com"
                ),
        Project(idProject=16,
                nameProject= "Meals and Medicine for Venezuelan Hospitals",
                statusProject= "In Progress",
                shortDescription = "Providing new mothers and vulnerable patients in Venezuela with the nutrition, services, and medicine they deserve.",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 10000,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project1.com"
                ),

        Project(idProject=17,
                nameProject= "Emergency Hunger Relief in South Africa",
                statusProject= "finished",
                shortDescription = "Ensuring vulnerable families in rural South Africa keep food on the table during the COVID19 crisis..",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 2500,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project2.com"
                ),

        Project(idProject=18,
                nameProject= "Fresh Water for Children Displaced by Boko Haram in Nigeria",
                statusProject= "In Progress",
                shortDescription = "Provide water for up to 200 ChildVoice students living in Nigeria’s Malkohi Internally Displaced Persons (IDP) camp",
                amountProject=random.randint(0, 2000),
                shouldAmountProject= 3300,
                paymentInformationProject="some Payment informations ",
                pageProject= "www.Project3.com"
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

    projects[12].idImage = images[3].idImage
    projects[12].idNGO =ngos[2].idNGO

    projects[13].idImage = images[4].idImage
    projects[13].idNGO =ngos[2].idNGO

    projects[14].idImage = images[2].idImage
    projects[14].idNGO =ngos[2].idNGO

    projects[15].idImage = images[4].idImage
    projects[15].idNGO =ngos[2].idNGO

    projects[16].idImage = images[1].idImage
    projects[16].idNGO =ngos[2].idNGO

    projects[17].idImage = images[3].idImage
    projects[17].idNGO =ngos[2].idNGO

    

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
