from __future__ import annotations


class SoftwareEngineer:
    """Base class representing a software engineer."""
    def __init__(self, name: str) -> None:
        """Initialize a software engineer with a name and empty skills."""
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        """Add a new skill to the engineer's skill set."""
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    """Class representing a frontend engineer with web-related skills."""
    def __init__(self, name: str) -> None:
        """Initialize frontend developer and add default web skills."""
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        """Create a simple HTML page and log the process."""
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    """Class representing a backend developer focused on APIs."""
    def __init__(self, name: str) -> None:
        """Initialize backend developer and add default server-side skills."""
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        """Create a powerful API endpoint and log the process."""
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    """Class representing an Android developer."""
    def __init__(self, name: str) -> None:
        """Initialize Android developer and add default mobile skills."""
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        """Create a smooth mobile application and log the process."""
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    """Class representing a developer with both Frontend and Backend skills."""
    def create_web_application(self) -> None:
        """Start the process of creating a full-featured web application."""
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
