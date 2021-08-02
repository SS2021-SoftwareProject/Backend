# This file is not a working function or executable data, just the structure for some random values.

from datetime import datetime
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
            fileImage=bin(42),
            descriptionImage="The answer to everything, probably",
            formatImage="jpg"),
        Image(idImage=2,
            fileImage=bin(69),
            descriptionImage="A nice image",
            formatImage="jpg"),
        Image(idImage=3,
            fileImage=bin(420),
            descriptionImage="Another nice image",
            formatImage="png"),
        Image(idImage=4,
            fileImage=bin(1337),
            descriptionImage="The best image",
            formatImage="png"),
        Image(idImage=5,
            fileImage=bin(666),
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
