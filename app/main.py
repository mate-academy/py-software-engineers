class SoftwareEngineer:
    skills = []
    def __init__(self, name: str) -> None:
        self.name = name
    
    def learn_skill(self, skills: str | list) -> None:
        SoftwareEngineer.skills.append(skills)

class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name) -> None:
        self.name = name
        self.skills += ["JavaScript", "HTML", "CSS",]
    
    def create_awesome_web_page(self) -> None:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"
    
class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name) -> None:
        self.name = name
        self.skills += ["Python", "SQL", "Django"]

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"

class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name) -> None:
        self.name = name
        self.skills += ["Java", "Android studio"]

    def create_smooth_mobile_app(self) -> None:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"
    
class FullStackDeveloper(FrontendDeveloper, BackendDeveloper, AndroidDeveloper):
    def __init__(self, name) -> None:
        self.name = name

    def create_web_application(self) -> None:
        self.create_awesome_web_page()
        self.create_powerful_api()
        self.create_smooth_mobile_app()
