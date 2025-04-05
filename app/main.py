class SoftwareEngineer:
    def __init__(self, name):
        self.name = name
        self.skills = []

    def code(self):
        print(f"{self.name} is coding...")

    def learn_skills(self, *skills):
        for skill in skills:
            self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def create_web_application(self):
        frontend = self.create_awesome_web_page()
        backend = self.create_powerful_api()
        return {
            "frontend": frontend,
            "backend": backend,
        }
