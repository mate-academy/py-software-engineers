class SoftwareEngineer:
    def __init__(self, name: str, skills: list = None) -> None:
        self.name = name
        self.skills = [] if skills is None else skills

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list = None) -> None:
        default_skills = ["JavaScript", "HTML", "CSS"]
        all_skills = default_skills + (skills or [])
        super().__init__(name, skills=all_skills)

    def create_awesome_web_page(self, ) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list = None) -> None:
        default_skills = ["Python", "SQL", "Django"]
        all_skills = default_skills + (skills or [])
        super().__init__(name, skills=all_skills)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list = None) -> None:
        default_skills = ["Java", "Android studio"]
        all_skills = default_skills + (skills or [])
        super().__init__(name, skills=all_skills)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
