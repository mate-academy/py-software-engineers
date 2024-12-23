from time import sleep 


class SoftwareEngineer:
    skills = []
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    def learn_skill(self, skill: str) -> None:
        self.__class__.skills.append(skill)

class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
    
    skills = ["JavaScript", "HTML", "CSS"]
    
    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        sleep(2)
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
    
    skills == ["Python", "SQL", "Django",]
    
    def create_awesome_web_page(self):
        print(f"{self.name} is creating an API...")
        sleep(2)
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
    
    skills = ["Java", "Android studio"]
    
    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        sleep(2)
        return "Ads every three swipes"

class FullstackDeveloper(SoftwareEngineer, BackendDeveloper, FrontendDeveloper):
    def __init__(self, name):
        super().__init__(name)
    
    def create_web_application(self):
        print(f"{self.name} is creating a web application...")
        sleep(2)
        create_powerful_api()
        create_awesome_web_page()