class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, new_skill: str) -> None:
        self.skills += [new_skill]


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def add_skills(self):
        for skill in ["JavaScript", "HTML", "CSS"]:
            self.learn_skill(skill)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def add_skills(self):
        for skill in ["Python", "SQL", "Django"]:
            self.learn_skill(skill)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        for skill in ["Java", "Android studio"]:
            self.learn_skill(skill)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        FrontendDeveloper.add_skills(self)
        BackendDeveloper.add_skills(self)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()

mike = FrontendDeveloper("Mike")

print(mike.skills)