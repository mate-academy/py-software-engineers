class SoftwareEngineer:

    def __init__(self, name, skills=[]):
        self.name = name
        self.skills = skills

    def learn_skill(self, skill):
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):

    def __init__(self, name, skills=["JavaScript", "HTML", "CSS"]):
        super().__init__(name, skills)

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):

    def __init__(self, name, skills=["Python", "SQL", "Django"]):
        super().__init__(name, skills)

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):

    def __init__(self, name, skills=["Java", "Android studio"]):
        super().__init__(name, skills)

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def __init__(self, name, skills=["JavaScript", "HTML", "CSS",
                                     "Python", "SQL", "Django"]):
        super().__init__(name, skills)

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        FullStackDeveloper.create_powerful_api(self)
        FullStackDeveloper.create_awesome_web_page(self)
        return "Ads every three swipes"
