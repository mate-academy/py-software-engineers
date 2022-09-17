class SoftwareEngineer:
    def __init__(self, name: str, skills=None):
        if skills is None:
            skills = []
        self.name = name
        self.skills = skills

    def learn_skill(self, skill: str):
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.skills.append("JavaScript")
        self.skills.append("HTML")
        self.skills.append("CSS")

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.skills.append("Python")
        self.skills.append("SQL")
        self.skills.append("Django")

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.skills.append("Java")
        self.skills.append("Android studio")

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        BackendDeveloper.create_powerful_api(self)
        FrontendDeveloper.create_awesome_web_page(self)
