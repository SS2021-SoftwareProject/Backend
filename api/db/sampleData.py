# This file is not a working function or executable data, just the structure for some random values.

from datetime import datetime
from db.dbStructure import Image, NGO, Problem, Project, Solution, Summary, Milestone, User, Payment
from typing import List

def add_sample_data():
    """
    Adds some sample data.
    Again, not a working function atm.
    :return: -
    """

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
            fileImage="https://i.pinimg.com/originals/48/d4/52/48d452d6a198414702768488832801fe.jpg",
            descriptionImage="The answer to everything, probably",
            formatImage="jpg"),
        Image(idImage=2,
            fileImage="https://i.pinimg.com/originals/36/ae/42/36ae42ce13358d130b7fb12eecb2155c.jpg",
            descriptionImage="A nice image",
            formatImage="jpg"),
        Image(idImage=3,
            fileImage="https://www.sternsinger.de/fileadmin/_processed_/a/a/csm_Suedsudan_DorfNyanbath_Harms_102_web_2f554d068a.jpg",
            descriptionImage="Another nice image",
            formatImage="jpg"),
        Image(idImage=4,
            fileImage="https://unicef.at/fileadmin/_processed_/b/9/csm_UNICEF-kind-leerer-teller-UN0345138_d78780f7b6.jpg",
            descriptionImage="The best image",
            formatImage="jpg"),
        Image(idImage=5,
            fileImage="https://www.malteser-international.org/fileadmin/_processed_/8/4/csm_Hungerndes-Kind-bekommt-Zusatznahrung_f7e0c23dc3.jpg",
            descriptionImage="Don't use this image",
            formatImage="jpg"),
    ]

    # fictional user, sample data. Keys generated randomly from hex values. No logic.

    user: List[User] = [
        User(idUser=1,
            firstNameUser="Max",
            lastNameUser="Mustermann",
            emailUser="Max.Mustermann@example.com",
            passwordtokenuser="123456",
            publickeyUser="0xEFc80dD88d34DdaeAa4dF3E5c2feE45b08e7F19CEB",
            privatkeyUser="0x8DA75ea6aBb332c0e1FF0b67DBCfD3cfCEfaF975Cf",
            registryAtUser=datetime(2000, 2, 20),
            balanceUser=42),
        User(idUser=2,
            firstNameUser="Peter",
            lastNameUser="Python",
            emailUser="Peter.Python@example.com",
            passwordtokenuser="1652051816252081514",
            publickeyUser="0x94bC0bDcaDB2c6FCABdc8F6C448BeBAf77dec0147A",
            privatkeyUser="0x17AF21Ed5D93eaDAa39E2b831FDCcbcc4e0dDCDc9d",
            registryAtUser=datetime(2008, 8, 8),
            balanceUser=420),
        User(idUser=3,
            firstNameUser="Juliana",
            lastNameUser="Java",
            emailUser="Juliana.Java@example.com",
            passwordtokenuser="10211291141101221",
            publickeyUser="0xEaA6334C62ad3AB31aCA929A4AAf58A8eF374496FF",
            privatkeyUser="0xc67b269FAC37b74CBfeaEcae5F06aCd0F8f8eBa754",
            registryAtUser=datetime(1996, 11, 5),
            balanceUser=666),
        User(idUser=4,
            firstNameUser="Christian",
            lastNameUser="Cplusplus",
            emailUser="Christian.Cplusplus@example.com",
            passwordtokenuser="381891920911431612211916122119",
            publickeyUser="0x1813FDa8401259FCBaF4fbE435685Ef553ba86747D",
            privatkeyUser="0xb750f4D1721AFcf4CDc4dCdD349C8a70DD4ffdfc7f",
            registryAtUser=datetime(2002, 11, 15),
            balanceUser=1337),
        User(idUser=5,
            firstNameUser="Henrik",
            lastNameUser="Haskell",
            emailUser="Max.Mustermann@example.com",
            passwordtokenuser="85141891181191151212",
            publickeyUser="0xf05e166Efb85AA602c8AFcDf2E8A7f0B0cDc81a42a",
            privatkeyUser="0xFA2A0E0E7291FfC47d85EC5Ba097dae6BFa152d9EA",
            registryAtUser=datetime(2005, 9, 4),
            balanceUser=69),
    ]

    # fictional payment, sample data

    payments: List[Payment] = [
        Payment(idPayment=1,
            amountPayment=69,
            statePaynment="completed",
            datePayment=datetime(2020, 3, 7)),
        Payment(idPayment=2,
            amountPayment=420,
            statePaynment="completed",
            datePayment=datetime(2019, 4, 18)),
        Payment(idPayment=3,
            amountPayment=1337,
            statePaynment="completed",
            datePayment=datetime(2016, 1, 7)),
        Payment(idPayment=4,
            amountPayment=42,
            statePaynment="completed",
            datePayment=datetime(2012, 9, 4)),
        Payment(idPayment=5,
            amountPayment=666,
            statePaynment="completed",
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
        Summary(idSummery =1,
                descriptionSummery="A summary of the project Nr.1"),
        Summary(idSummery =2,
                descriptionSummery="A summary of the project Nr.2"),
        Summary(idSummery =3,
                descriptionSummery="A summary of the project Nr.3")
    
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
                amountProject=500,
                shouldAmountProject= 10000,
                paymentInformationProject="some Payment informations ",
                shortDescription = "Kurzer Text",
                pageProject= "www.Project1.com"
                ),

        Project(idProject=2,
                nameProject= "Test Project Nr.2",
                statusProject= "finished",
                amountProject=5000,
                shouldAmountProject= 5000,
                paymentInformationProject="some Payment informations ",
                shortDescription = "Kurzer Text2",
                pageProject= "www.Project2.com"
                ),

        Project(idProject=3,
                nameProject= "Test Project Nr.3",
                statusProject= "almost finished",
                amountProject=2500,
                shouldAmountProject= 3000,
                paymentInformationProject="some Payment informations ",
                shortDescription = "Kurzer Text3",
                pageProject= "www.Project3.com"
                )

    ]

    # foreign key assignments for projects

    projects[0].idImage = images[0].idImage
    projects[0].idNGO =ngos[0].idNGO
    projects[0].idProblem=problems[0].idProblem
    projects[0].idSolution= solutions[0].idSolution
    projects[0].idSummary = summaries[0].idSummary 

    projects[1].idImage = images[1].idImage
    projects[1].idNGO =ngos[1].idNGO
    projects[1].idProblem=problems[1].idProblem
    projects[1].idSolution= solutions[1].idSolution
    projects[1].idSummary = summaries[1].idSummary 

    projects[2].idImage = images[2].idImage
    projects[2].idNGO =ngos[2].idNGO
    projects[2].idProblem=problems[2].idProblem
    projects[2].idSolution= solutions[2].idSolution
    projects[2].idSummary = summaries[2].idSummary 



    

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

    payments[0].idUser = user[0].idUser
    payments[1].idUser = user[1].idUser
    payments[2].idUser = user[2].idUser
    payments[3].idUser = user[3].idUser
    payments[4].idUser = user[4].idUser

    payments[0].idProject = projects[0].idProject
    payments[1].idProject = projects[1].idProject
    payments[2].idProject = projects[2].idProject
    payments[3].idProject = projects[3].idProject
    payments[4].idProject = projects[4].idProject
