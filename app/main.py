class SoftwareEngineer:
    skills = []
    def __init__(self, name: str) -> None:
        self.name = name

    def learn_skill(self, skill: str) -> None:
        SoftwareEngineer.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str,
                 skills:
                 list=["JavaScript", "HTML", "CSS"]) -> None:
        super().__init__(name)
        self.skills = skills

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str,
                 skills: list=["Python", "SQL", "Django"]) -> None:
        super().__init__(name)

    def create_powerful_api(self) ->str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"

    
class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str,
                 skills: list=["Java", "Android studio"]) -> None:
        super().__init__(name)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str,
                 skills: list = ["JavaScript", "HTML", "CSS",
                    "Python", "SQL", "Django"]) -> None
        super().__init__(name, skills)
  
    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        create_powerful_api()
        create_awesome_web_page()