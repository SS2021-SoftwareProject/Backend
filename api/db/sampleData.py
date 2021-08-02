# This file is not a working function or executable data, just the structure for some random values.


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
