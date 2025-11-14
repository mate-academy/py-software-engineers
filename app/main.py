class SoftwareEngineer:

    base_skills = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

        self.skills.extend(self.base_skills)

    def learn_skill(self, skill: str) -> None:
        self.skills += [skill]


class FrontendDeveloper(SoftwareEngineer):
    base_skills = ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    base_skills = ["Python", "SQL", "Django"]

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    base_skills = ["Java", "Android studio"]

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(
    BackendDeveloper,
    FrontendDeveloper
):
    base_skills = BackendDeveloper.base_skills + FrontendDeveloper.base_skills

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
