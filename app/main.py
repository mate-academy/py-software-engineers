class SoftwareEngineer:
    skills = []
    def __init__(self, name: str) -> None:
        self.name = name

    def learn_skill(skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        self.super().__init__(name)
        self.skills += ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page() -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        self.super().__init__(name)
        self.skills += ["Python", "SQL", "Django"]

    def create_powerful_api() -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        self.super().__init__(name)
        self.skills.append("Java")
        self.skills.append("Android studio")

    def create_smooth_mobile_app() -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str) -> None:
        SoftwareEngineer.__init__(self, name)
        self.skills += ["Python", "SQL", "Django", "JavaScript", "HTML", "CSS"]

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
