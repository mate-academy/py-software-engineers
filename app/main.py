class SoftwareEngineer:
    _default_skills = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)

    @classmethod
    def set_default_skills(cls, engineer: "SoftwareEngineer") -> None:
        for skill in cls._default_skills:
            engineer.learn_skill(skill)


class FrontendDeveloper(SoftwareEngineer):
    _default_skills = ["JavaScript", "HTML", "CSS"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        FrontendDeveloper.set_default_skills(self)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    _default_skills = ["Python", "SQL", "Django"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        BackendDeveloper.set_default_skills(self)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    _default_skills = ["Java", "Android studio"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        AndroidDeveloper.set_default_skills(self)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
