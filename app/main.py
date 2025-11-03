"""
Module for software engineer class hierarchy.

This module provides a comprehensive class structure for different types
of software engineers, including frontend, backend, Android, and full-stack
developers. Each class represents a specialized role with unique skills
and capabilities.

Classes:
    SoftwareEngineer: Base class for all software engineers.
    FrontendDeveloper: Specializes in web frontend development.
    BackendDeveloper: Specializes in server-side development.
    AndroidDeveloper: Specializes in Android mobile app development.
    FullStackDeveloper: Combines frontend and backend development skills.

Example:
    >>> engineer = SoftwareEngineer("Max")
    >>> engineer.learn_skill("Python")
    >>> print(engineer.skills)
    ['Python']

    >>> full_stack = FullStackDeveloper("Tom")
    >>> full_stack.create_web_application()
    Tom started creating a web application...
    Tom is creating an API...
    Tom is creating a webpage...
"""


class SoftwareEngineer:
    """
    Base class representing a software engineer.

    This class serves as a parent for all specialized engineer types.
    Engineers have a name and a list of skills that can be expanded
    through learning.

    Attributes:
        name (str): The name of the software engineer.
        skills (list[str]): A list of skills the engineer possesses.
                           Initially empty, populated by child classes
                           or through the learn_skill method.

    Example:
        >>> engineer = SoftwareEngineer("Max")
        >>> engineer.skills
        []
        >>> engineer.learn_skill("Python")
        >>> engineer.skills
        ['Python']
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a SoftwareEngineer instance.

        Creates a new software engineer with the given name and
        an empty skills list.

        Args:
            name (str): The name of the software engineer.

        Returns:
            None
        """
        self.name = name
        self.skills: list[str] = []

    def learn_skill(self, skill: str) -> None:
        """
        Add a new skill to the engineer's skill list.

        Appends the provided skill to the engineer's existing
        list of skills. This method allows engineers to expand
        their capabilities over time.

        Args:
            skill (str): The skill to be added to the skills list.
                        Can be any technology, framework, or language.

        Returns:
            None

        Example:
            >>> engineer = SoftwareEngineer("Max")
            >>> engineer.learn_skill("Python")
            >>> engineer.learn_skill("Docker")
            >>> engineer.skills
            ['Python', 'Docker']
        """
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    """
    A frontend developer specializing in web interfaces.

    This class represents a software engineer focused on frontend development,
    with default skills in JavaScript, HTML, and CSS. Frontend developers
    are responsible for creating user-facing web interfaces and experiences.

    Inherits from:
        SoftwareEngineer: Base class providing name and skill management.

    Attributes:
        name (str): The name of the frontend developer.
        skills (list[str]): List of skills automatically including
                           JavaScript, HTML, and CSS upon initialization.

    Example:
        >>> front_dev = FrontendDeveloper("Alisa")
        >>> front_dev.skills
        ['JavaScript', 'HTML', 'CSS']
        >>> page = front_dev.create_awesome_web_page()
        Alisa is creating a webpage...
        >>> page
        '<h1>Hello world</h1>'
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a FrontendDeveloper instance.

        Creates a new frontend developer with the given name and
        automatically adds core frontend skills (JavaScript, HTML, CSS)
        to their skill list.

        Args:
            name (str): The name of the frontend developer.

        Returns:
            None
        """
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        """
        Create a simple web page.

        Simulates the process of creating a web page by printing
        a status message and returning basic HTML code. This method
        demonstrates the core capability of a frontend developer.

        Prints:
            "{name} is creating a webpage..." to stdout.

        Returns:
            str: HTML code for a simple webpage with "Hello world" heading.
                 Returns '<h1>Hello world</h1>'.

        Example:
            >>> front_dev = FrontendDeveloper("Alisa")
            >>> page = front_dev.create_awesome_web_page()
            Alisa is creating a webpage...
            >>> page
            '<h1>Hello world</h1>'
        """
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    """
    A backend developer specializing in server-side development.

    This class represents a software engineer focused on backend development,
    with default skills in Python, SQL, and Django. Backend developers
    handle server logic, databases, and API development.

    Inherits from:
        SoftwareEngineer: Base class providing name and skill management.

    Attributes:
        name (str): The name of the backend developer.
        skills (list[str]): List of skills automatically including
                           Python, SQL, and Django upon initialization.

    Example:
        >>> backend_dev = BackendDeveloper("Bob")
        >>> backend_dev.skills
        ['Python', 'SQL', 'Django']
        >>> api = backend_dev.create_powerful_api()
        Bob is creating an API...
        >>> api
        'http://127.0.0.1:8000'
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a BackendDeveloper instance.

        Creates a new backend developer with the given name and
        automatically adds core backend skills (Python, SQL, Django)
        to their skill list.

        Args:
            name (str): The name of the backend developer.

        Returns:
            None
        """
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        """
        Create a powerful API.

        Simulates the process of creating a RESTful API by printing
        a status message and returning the local development server address.
        This method demonstrates the core capability of a backend developer.

        Prints:
            "{name} is creating an API..." to stdout.

        Returns:
            str: The local API address where the API is hosted.
                 Returns 'http://127.0.0.1:8000'.

        Example:
            >>> backend_dev = BackendDeveloper("Bob")
            >>> address = backend_dev.create_powerful_api()
            Bob is creating an API...
            >>> address
            'http://127.0.0.1:8000'
        """
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    """
    An Android developer specializing in mobile app development.

    This class represents a software engineer focused on Android development,
    with default skills in Java and Android Studio. Android developers
    create mobile applications for the Android platform.

    Inherits from:
        SoftwareEngineer: Base class providing name and skill management.

    Attributes:
        name (str): The name of the Android developer.
        skills (list[str]): List of skills automatically including
                           Java and Android studio upon initialization.

    Example:
        >>> android_dev = AndroidDeveloper("Beth")
        >>> android_dev.skills
        ['Java', 'Android studio']
        >>> app = android_dev.create_smooth_mobile_app()
        Beth is creating a mobile app...
        >>> app
        'Ads every three swipes'
    """

    def __init__(self, name: str) -> None:
        """
        Initialize an AndroidDeveloper instance.

        Creates a new Android developer with the given name and
        automatically adds core Android development skills (Java,
        Android studio) to their skill list.

        Args:
            name (str): The name of the Android developer.

        Returns:
            None
        """
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        """
        Create a smooth mobile application.

        Simulates the process of creating an Android mobile app by printing
        a status message and returning a humorous description of the app's
        user experience strategy. This method demonstrates the core capability
        of an Android developer.

        Prints:
            "{name} is creating a mobile app..." to stdout.

        Returns:
            str: Description of the app's UX monetization strategy.
                 Returns 'Ads every three swipes'.

        """
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    """
    A full-stack developer with both frontend and backend expertise.

    This class uses multiple inheritance to combine the skills and methods
    of both BackendDeveloper and FrontendDeveloper. A full-stack developer
    can handle all aspects of web application development, from server-side
    logic to user interface design.

    Inherits from:
        BackendDeveloper: Provides backend skills and API creation capability.
        FrontendDeveloper: Provides frontend skills and webpage
        creation capability.

    Note:
        Due to Python's Method Resolution Order (MRO),
            backend skills are
        inherited and added to the skills list first, followed by frontend
        skills. This is determined by the order of parent classes in
        the inheritance declaration.

    Attributes:
        name (str): The name of the full-stack developer.
        skills (list[str]): Combined list of backend and frontend skills.
                           Includes: Python, SQL, Django,
                           JavaScript, HTML, CSS.

    """

    def create_web_application(self) -> None:
        """
        Create a complete web application.

        This method orchestrates the creation of both the backend API
        and frontend webpage by calling the respective methods inherited
        from parent classes. It represents the full-stack developer's
        ability to build end-to-end web applications.

        The method performs the following steps:
        1. Prints a startup message indicating work has begun
        2. Creates the backend API (calls create_powerful_api)
        3. Creates the frontend webpage (calls create_awesome_web_page)

        Prints:
            "{name} started creating a web application..." to stdout,
            followed by messages from create_powerful_api and
            create_awesome_web_page methods.

        Returns:
            None
        """
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
