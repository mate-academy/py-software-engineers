class SoftwareEngineer:
    def __init__(self, name: str):
        self.name = name

    skills = []

    def learn_skill(self, skill: str):
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super(FrontendDeveloper, self).__init__(
            name=name
        )

    skills = ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super(BackendDeveloper, self).__init__(
            name=name
        )

    skills = ["Python", "SQL", "Django"]

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super(AndroidDeveloper, self).__init__(
            name=name
        )

    skills = ["Java", "Android studio"]

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name):
        super(FullStackDeveloper, self).__init__(
            name=name
        )
        self.skills = FrontendDeveloper.skills + BackendDeveloper.skills

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
