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
        Initializes the engineer's name and manages the skills they
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


class FrontendDeveloper(SoftwareEngineer):
    """
    It represents a frontend developer who can create web pages.
    """

    def __init__(
        self,
        name: str
    ) -> None:
        """
        Initializes the developer's name and manages the skills they learned.

        Attributes:
            name (str): Developer's name.
            skills (list[str]): Skills learned.
        """
        super().__init__(name)
        self.skills += ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page(
        self
    ) -> str:
        """
        Displays a message in the console and returns the webpage HTML.

        Returns:
            str: The HTML code of the created webpage.
        """
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"
