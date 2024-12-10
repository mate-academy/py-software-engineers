class SoftwareEngineer:

    def __init__(self, name: str) -> None:
        self.name = name
        if "skills" not in self.__dict__:
            self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:
        if "skills" in self.__dict__:
            self.skills += ["JavaScript", "HTML", "CSS"]
        else:
            self.skills = ["JavaScript", "HTML", "CSS"]
        super().__init__(name)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:
        self.skills = ["Python", "SQL", "Django"]
        super().__init__(name)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:
        self.skills = ["Java", "Android studio"]
        super().__init__(name)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api(), self.create_awesome_web_page()
