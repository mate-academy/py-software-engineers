from typing import Optional


class SoftwareEngineer:
    def __init__(self, name: str, skills: Optional[list] = None) -> None:
        self.name = name
        self.skills = skills if skills is not None else []

    def learn_skill(self, skill: str = None) -> None:
        if skill is not None:
            self.skills.append(skill)
        else:
            self.skills.append("Python")
            self.skills.append("JavaScript")


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name, skills=["JavaScript", "HTML", "CSS"])

    def learn_skill(self, skills: str = None) -> None:
        self.skills.append(skills)

    def create_awesome_web_page(self, name: Optional[str] = None) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name, skills=["Python", "SQL", "Django"])

    def learn_skill(self, skills: str = None) -> None:
        self.skills.append(skills)

    def create_powerful_api(self, name: Optional[str] = None) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name, skills=["Java", "Android studio"])

    def learn_skill(self, skills: str = None) -> None:
        self.skills.append(skills)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name, skills=["Python", "SQL",
                                       "Django", "JavaScript", "CSS", "HTML"])

    def create_powerful_api(self) -> str:
        return BackendDeveloper.create_powerful_api(self, "Powerful API")

    def create_awesome_web_page(self, name: Optional[str] = None) -> str:
        return FrontendDeveloper.create_awesome_web_page(self, name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
