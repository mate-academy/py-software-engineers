class SoftwareEngineer:
    skills = []

    def __init__(self, name):
        self.name = name

    def learn_skill(self, skill):
        SoftwareEngineer.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    skills = ["JavaScript", "HTML", "CSS"]

    def __init__(self, name):
        super().__init__(name)

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"

    def learn_skill(self, skill):
        FrontendDeveloper.skills.append(skill)


class BackendDeveloper(SoftwareEngineer):
    skills = ["Python", "SQL", "Django"]

    def __init__(self, name):
        super().__init__(name)

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"

    def learn_skill(self, skill):
        BackendDeveloper.skills.append(skill)


class AndroidDeveloper(SoftwareEngineer):
    skills = ["Java", "Android studio"]

    def __init__(self, name):
        super().__init__(name)

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"

    def learn_skill(self, skill):
        AndroidDeveloper.skills.append(skill)


class FullStackDeveloper(BackendDeveloper,
                         FrontendDeveloper,
                         SoftwareEngineer):

    skills = ["Python", "SQL", "Django", "JavaScript", "HTML", "CSS"]

    def __init__(self, name):
        super().__init__(name)

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        BackendDeveloper.create_powerful_api(self)
        FrontendDeveloper.create_awesome_web_page(self)

    def learn_skill(self, skill):
        FullStackDeveloper.skills.append(skill)
