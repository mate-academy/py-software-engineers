class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        dev_front = ["JavaScript", "HTML", "CSS"]
        self.skills.extend(dev_front)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        page = "<h1>Hello world</h1>"
        return page


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        dev_back = ["Python", "SQL", "Django"]
        self.skills.extend(dev_back)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        address = "http://127.0.0.1:8000"
        return address


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        dev_mobile = ["Java", "Android studio"]
        self.skills.extend(dev_mobile)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        app = "Ads every three swipes"
        return app


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
