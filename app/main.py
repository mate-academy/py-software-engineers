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
        skill: str
    ) -> None:
        """
        Stores the computer skill that the engineer learned.

        Args:
            skill (str): the skill learned.
        """
        self.skills.append(skill)


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


class BackendDeveloper(SoftwareEngineer):
    """
    It represents a backend developer who can create APIs.
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
        self.skills += ["Python", "SQL", "Django"]

    def create_powerful_api(
        self
    ) -> str:
        """
        Displays a message in the console and returns the API's address.

        Returns:
            str: the address of the API.
        """
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    """
    It represents an android developer who can create apps.
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
        self.skills += ["Java", "Android studio"]

    def create_smooth_mobile_app(
        self
    ) -> str:
        """
        Displays a message in the console and returns UX of the created app.

        Returns:
            str: The UX.
        """
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    """
    It represents a fullstack developer who can create web apps.
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

    def create_web_application(
        self
    ) -> None:
        """
        Displays a message in the console.
        """
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
