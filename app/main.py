class SoftwareEngineer:
    def __init__(self, name: str, skills: list = None):
        self.name = name
        self.skills = skills
        if skills is None:
            self.skills = []

    def learn_skill(self, skill):
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list = None):
        if skills is None:
            skills = ["JavaScript", "HTML", "CSS"]
        super().__init__(name, skills)


    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        page = "<h1>Hello world</h1>"
        return page


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list = None):
        if skills is None:
            skills = ["Python", "SQL", "Django"]
        super().__init__(name, skills)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        address = "http://127.0.0.1:800"
        return address


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list = None):
        if skills is None:
            skills = ["Java", "Android studio"]
        super().__init__(name, skills)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        app = "Ads every three swipes"
        return app


class FullStackDeveloper(BackendDeveloper, AndroidDeveloper):
    def __init__(self, name: str, skills: list = None):
        if skills is None:
            skills = ["Python", "SQL", "Django",
                           "JavaScript", "HTML", "CSS"]
        super().__init__(name, skills)

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_smooth_mobile_app()