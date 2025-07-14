class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloperMixin:
    def add_frontend(self) -> None:
        dev_skills = ["JavaScript", "HTML", "CSS"]
        for skill in dev_skills:
            self.learn_skill(skill)


class BackendDeveloperMixin:
    def add_backend(self) -> None:
        dev_skills = ["Python", "SQL", "Django"]
        for skill in dev_skills:
            self.learn_skill(skill)


class AndroidDeveloperMixin:
    def add_android(self) -> None:
        dev_skills = ["Java", "Android studio"]
        for skill in dev_skills:
            self.learn_skill(skill)


class FrontendDeveloper(SoftwareEngineer, FrontendDeveloperMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.add_frontend()

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer, BackendDeveloperMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.add_backend()

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer, AndroidDeveloperMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.add_android()

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
