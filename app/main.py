class SoftwareEngineer:
    """
    Represents base Software Engineer.

    Attributes:
    ----------
    name : str
        the name of the Software Engineer

    Methods:
    _______
    learn_skills()
        adds a new learned skill
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        """
        Adds a new learned skill to the total skill set.
        :param skill: str
        :return: None
        """
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(("JavaScript", "HTML", "CSS"))

    def create_awesome_web_page(self) -> str:
        """
        Displays an info message and returns the code of the created webpage.
        :return: str
        """
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(("Python", "SQL", "Django"))

    def create_powerful_api(self) -> str:
        """
        Displays an info message and returns the address of the API.
        :return: str
        """
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(("Java", "Android studio"))

    def create_smooth_mobile_app(self) -> str:
        """
        Displays an info message and returns the UX of the created app.
        :return: str
        """
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_web_application(self) -> None:
        """
        Displays an info message and creates API, Web Page.
        :return: str
        """
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
