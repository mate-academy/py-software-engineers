class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendSkillsMixin:
    @staticmethod
    def f_skills_extend(ls: list) -> None:
        ls.extend(["JavaScript", "HTML", "CSS"])


class BackendSkillsMixin:
    @staticmethod
    def b_skills_extend(ls: list) -> None:
        ls.extend(["Python", "SQL", "Django"])


class FrontendDeveloper(SoftwareEngineer, FrontendSkillsMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self.f_skills_extend(self.skills)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer, BackendSkillsMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self.b_skills_extend(self.skills)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper,
                         BackendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
