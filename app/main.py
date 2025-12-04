from typing import List


class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.skills: List[str] = []
        self._add_default_skills()

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)

    def _add_default_skills(self) -> None:
        pass


class FrontendDeveloper(SoftwareEngineer):
    def _add_default_skills(self) -> None:
        super()._add_default_skills()
        self.skills.extend(["JavaScript", "CSS", "HTML"])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def _add_default_skills(self) -> None:
        super()._add_default_skills()
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def _add_default_skills(self) -> None:
        super()._add_default_skills()
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
