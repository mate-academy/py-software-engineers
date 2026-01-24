class SoftwareEngineer:
    """
    It represents a generic software engineer who can learn new
    software skills.
    """

    def __init__(
            self,
            name: str
    ) -> None:
        """
        Initializes the engineer's name and manages the skills he
        can learn.

        Attributes:
            name (str): The engineer's name.
            skills (list[str]): Skill or skills that the engineer learned.
        """
        self.name = name
        self.skills = []

    def learn_skill(
        self,
        new_skill: str
    ) -> None:
        """
        Stores the computer skill that the engineer learned.

        Args:
            new_skill (str): the skill learned.
        """
        self.skills.append(new_skill)
