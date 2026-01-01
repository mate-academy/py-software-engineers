class SoftwareEngineer:
    def __init__(self, name: str):
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str):
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.skills.extend("JavaScript", "HTML", "CSS")

    def create_awsome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.skills.extend("Python", "SQL", "Django")

    def create_powerfull_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.skills.extend("Java", "Android studio")

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(SoftwareEngineer, BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str):
        super().__init__(name)
        self.skills.extend("Java", "Android studio")
        super().create_powerfull_api()
        super().create_awsome_web_page()

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
