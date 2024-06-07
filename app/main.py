class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class BackendDeveloperMixin:
    backend_skills = ["Python", "SQL", "Django"]

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class FrontendDeveloperMixin:
    frontend_skills = ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class FrontendDeveloper(FrontendDeveloperMixin, SoftwareEngineer):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = self.frontend_skills


class BackendDeveloper(BackendDeveloperMixin, SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = self.backend_skills


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["Java", "Android studio"]

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(
    BackendDeveloperMixin,
    FrontendDeveloperMixin,
    SoftwareEngineer
):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = self.frontend_skills + self.backend_skills

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
