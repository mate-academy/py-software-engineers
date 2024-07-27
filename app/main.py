class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class SkillMixin:
    def to_add_skills(self, list_skills: list) -> None:
        for skill in list_skills:
            self.learn_skill(skill)


class FrontendDeveloper(SoftwareEngineer, SkillMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.to_add_skills(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer, SkillMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.to_add_skills(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer, SkillMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.to_add_skills(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
