class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills += ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        page = "<h1>Hello world</h1>"
        return page


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills += ["Python", "SQL", "Django"]

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        api = "http://127.0.0.1:8000"
        return api


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills += ["Java", "Android studio"]

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        app = "Ads every three swipes"
        return app


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
