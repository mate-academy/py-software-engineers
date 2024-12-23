from time import sleep 


class SoftwareEngineer:
    def __init__(self, name: str, skills: list) -> None:
        self.name = name
        self.skills = skills
    
    def learn_skill(self, skill: str) -> None:
        self.__class__.skills.append(skill)

class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name, skills):
        super().__init__(name, skills)
    
    skills = ["JavaScript", "HTML", "CSS"]
    
    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        sleep(2)
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name, skills):
        super().__init__(name, skills)
    
    skills = ["Python", "SQL", "Django",]
    
    def create_awesome_web_page(self):
        print(f"{self.name} is creating an API...")
        sleep(2)
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name, skills):
        super().__init__(name, skills)
    
    skills = ["Java", "Android studio"]
    
    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        sleep(2)
        return "Ads every three swipes"

class FullstackDeveloper(SoftwareEngineer, BackendDeveloper, FrontendDeveloper):
    def __init__(self, name, skills):
        super().__init__(name, skills)    
    
    def create_web_application(self):
        print(f"{self.name} is creating a web application...")
        sleep(2)
        BackendDeveloper.create_powerful_api()
        FrontendDeveloper.create_awesome_web_page()