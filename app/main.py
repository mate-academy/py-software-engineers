class SoftwareEngineer:
    """
    Represents a software engineer
    with a name and a list of skills.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a SoftwareEngineer instance.

        Args:
            name: The name of the engineer.
        """
        self.name = name
        self.skills = list()

    def learn_skill(self, skill: str) -> None:
        """
        Adds a skill to the engineer's skill list.

        Args:
            skill: The skill to learn.
        """
        if skill not in self.skills:
            self.skills.append(skill)

    def default_skills(self, *default_skills: str) -> None:
        """
        Adds a list of default skills
        to the engineer's skill list.

        Args:
            default_skills: A list of skills to add.
        """
        self.skills += [
            skill
            for skill in default_skills
            if skill not in self.skills
        ]


class FrontendDeveloper(SoftwareEngineer):
    """
    Represents a frontend developer,
    a specialized type of software engineer.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a FrontendDeveloper instance.

        Args:
            name: The name of the developer.
        """
        super().__init__(name)
        self.default_skills("JavaScript", "HTML", "CSS")

    def create_awesome_web_page(self) -> str:
        """
        Creates an awesome web page.

        Returns:
            The HTML code of the web page.
        """
        print(f"{self.name} is creating a webpage...")

        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    """
    Represents a backend developer,
    a specialized type of software engineer.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a BackendDeveloper instance.

        Args:
            name: The name of the developer.
        """
        super().__init__(name)
        self.default_skills("Python", "SQL", "Django")

    def create_powerful_api(self) -> str:
        """
        Creates a powerful API.

        Returns:
            The address of the API.
        """
        print(f"{self.name} is creating an API...")

        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    """
    Represents an Android developer,
    a specialized type of software engineer.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes an AndroidDeveloper instance.

        Args:
            name: The name of the developer.
        """
        super().__init__(name)
        self.default_skills("Java", "Android studio")

    def create_smooth_mobile_app(self) -> str:
        """
        Creates a smooth mobile app.

        Returns:
            The UX of the created app.
        """
        print(f"{self.name} is creating a mobile app...")

        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    """
    Represents a full-stack developer,
    a combination of backend and frontend.
    """

    def create_web_application(self) -> None:
        """
        Creates a web application by creating an API and a web page.
        """
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
