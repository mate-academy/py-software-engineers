from typing import List


class SoftwareEngineer:
    
    skills: List[str] = []
    
    def __init__(self, name: str) -> None:
        self.name = name
        
    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    
    skills: List[str] = ["JavaScript", "HTML", "CSS"]
    
    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    
    skills: List[str] = ["Python", "SQL", "Django"]
    
    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    
    skills: List[str] = ["Java", "Android studio"]
    
    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    
    skills: List[str] = BackendDeveloper.skills + FrontendDeveloper.skills
    
    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        
        self.create_powerful_api()
        self.create_awesome_web_page()
