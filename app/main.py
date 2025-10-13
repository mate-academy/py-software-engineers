class SoftwareEngineer:
    def __init__(self, name: str, skills=None) -> None:  # noqa: ANN001
        self.name = name
        self.skills = skills if skills is not None else []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:
        super().__init__(name, ["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:
        super().__init__(name, ["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:
        super().__init__(name, ["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def __init__(self, name: str) -> None:
        backend_skills = ["Python", "SQL", "Django"]
        frontend_skills = ["JavaScript", "HTML", "CSS"]
        default_skills = backend_skills + frontend_skills
        SoftwareEngineer.__init__(self, name, default_skills)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        BackendDeveloper.create_powerful_api(self)
        FrontendDeveloper.create_awesome_web_page(self)
