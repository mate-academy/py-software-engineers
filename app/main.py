class SoftwareEngineer:

    def __init__(self, name: str, skills=[]):
        self.name = name
        self.skills = skills
        if isinstance(self, FrontendDeveloper):
            self.skills = ["JavaScript", "HTML", "CSS"]
        if isinstance(self, BackendDeveloper):
            self.skills = ["Python", "SQL", "Django"]
        if isinstance(self, AndroidDeveloper):
            self.skills = ["Java", "Android studio"]
        if isinstance(self, FullStackDeveloper):
            self.skills = ["Python", "SQL", "Django",
                           "JavaScript", "CSS", "HTML"]

    def learn_skill(self, skill: str):
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super(FrontendDeveloper, self).__init__(name)

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):

    def __init__(self, name):
        super(BackendDeveloper, self).__init__(name)

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):

    def __init__(self, name):
        super(AndroidDeveloper, self).__init__(name)

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper,
                         BackendDeveloper,
                         AndroidDeveloper):

    def __init__(self, name):
        super(FullStackDeveloper, self).__init__(name)

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
