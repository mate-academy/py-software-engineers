from typing import List


class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills: List[str] = []

    def learn_skill(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    DEFAULT_SKILLS = ["JavaScript", "CSS", "HTML"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = self.DEFAULT_SKILLS.copy()

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    DEFAULT_SKILLS = ["Python", "SQL", "Django"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = self.DEFAULT_SKILLS.copy()

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    DEFAULT_SKILLS = ["Java", "Android studio"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = self.DEFAULT_SKILLS.copy()

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = BackendDeveloper.DEFAULT_SKILLS.copy() + FrontendDeveloper.DEFAULT_SKILLS.copy()

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        print(f"{self.name} is creating an API...")
        print(f"{self.name} is creating a webpage...")
