class SoftwareEngineer:
    skills: list[str] = []

    def __init__(self, name: str) -> None:
        self.name = name

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    skills: list[str] = ["JavaScript", "HTML", "CSS"]
    skills.extend(SoftwareEngineer.skills)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    skills: list[str] = ["Python", "SQL", "Django"]
    skills.extend(SoftwareEngineer.skills)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    skills: list[str] = ["Java", "Android studio"]
    skills.extend(SoftwareEngineer.skills)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    skills: list[str] = []
    skills.extend(FrontendDeveloper.skills)
    skills.extend(BackendDeveloper.skills)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
