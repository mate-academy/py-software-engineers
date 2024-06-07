class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class BackendDeveloperMixin:
    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class FrontendDeveloperMixin:
    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class FrontendDeveloper(FrontendDeveloperMixin, SoftwareEngineer):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["JavaScript", "HTML", "CSS"]


class BackendDeveloper(BackendDeveloperMixin, SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["Python", "SQL", "Django"]


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["Java", "Android studio"]

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(
    FrontendDeveloperMixin,
    BackendDeveloper
):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills += ["JavaScript", "HTML", "CSS"]

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
