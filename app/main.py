class SoftwareEngineer:
    skills = []

    def __init__(self, name: str):
        self.name = name

    def learn_skill(self, skill):
        skills = self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    skills = ['JavaScript', "HTML", "CSS"]

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    skills = ["Python", "SQL", "Django"]

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    skills = ["Java", "Android studio"]

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    skills = BackendDeveloper.skills + FrontendDeveloper.skills

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
