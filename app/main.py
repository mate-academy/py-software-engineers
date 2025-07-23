class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendSkillsMixin:
    def add_frontend_skills(self) -> None:
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendSkillsMixin:
    def add_backend_skills(self) -> None:
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class FrontendDeveloper(SoftwareEngineer, FrontendSkillsMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.add_frontend_skills()


class BackendDeveloper(SoftwareEngineer, BackendSkillsMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.add_backend_skills()


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(
    SoftwareEngineer,
    BackendSkillsMixin,
    FrontendSkillsMixin
):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.add_backend_skills()
        self.add_frontend_skills()

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
