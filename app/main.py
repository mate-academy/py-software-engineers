class SoftwareEngineer:
    """
    Base class representing a generic software engineer.
    Responsibilities:
        - stores the engineer's name
        - maintains a personal list of skills
        - provides a method for learning new skills

    Attributes:
        name (str): Name of the engineer.
        skills (list[str]): Collection of acquired skills.
    """

    def __init__(self, name: str) -> None:
        self.skills: list[str] = []
        self.name = name

    def learn_skill(self, skill: str) -> None:
        """
        Adds a new skill to the engineer's skill list.

        :param skill: Name of the skill to learn.
        """

        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    """
    Software engineer specializing in frontend development.
    Adds default frontend-related skills:
        - JavaScript
        - HTML
        - CSS

    Provides tools to create basic webpage structures.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.skills.extend([
            "JavaScript",
            "HTML",
            "CSS",
        ])

    def create_awesome_web_page(self) -> str:
        """
        Creates HTML page.
            - prints an action message indicating webpage creation
            - returns the generated HTML code

        :return: HTML content of the created web page.
        """

        print(f"{self.name} is creating a webpage...")

        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    """
    Software engineer specializing in backend development.
    Adds default backend-related skills:
        - Python
        - SQL
        - Django

    Provides functionality to build backend API endpoints.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.skills.extend([
            "Python",
            "SQL",
            "Django",
        ])

    def create_powerful_api(self) -> str:
        """
        Creates a backend API endpoint.
        Actions:
            - prints an action message
            - returns the local URL of the created API

        :return: URL of the generated API endpoint.
        """

        print(f"{self.name} is creating an API...")

        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    """
    Software engineer specializing in Android mobile development.
    Adds default Android-related skills:
        - Java
        - Android studio

    Supports building basic mobile applications.
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.skills.extend([
            "Java",
            "Android studio",
        ])

    def create_smooth_mobile_app(self) -> str:
        """
        Creates a mobile application.
        Actions:
            - prints an action message
            - returns simulated UX description of the application

        :return: UX result of the created application.
        """

        print(f"{self.name} is creating a mobile app...")

        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    """
    Developer capable of working with both backend and frontend technologies.
    Responsibilities:
        - inherits backend and frontend skills
        - provides high-level method to build a complete web application

    Combines functionality from both BackendDeveloper and FrontendDeveloper.
    """

    def create_web_application(self) -> None:
        """
        Creates a complete web application.
        Process:
            - prints a start message
            - creates backend API
            - creates frontend webpage

        :return: None.
        """

        print(f"{self.name} started creating a web application...")

        self.create_powerful_api()
        self.create_awesome_web_page()
