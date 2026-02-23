class SoftwareEngineer():
    def __init__(self, name: str, skills: list[str] | None = None) -> None:
        self.name = name
        self.skills = skills or []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list[str] | None = None) -> None:
        if isinstance(skills, list):
            skills.extend(["JavaScript", "HTML", "CSS"])
        else:
            skills = ["JavaScript", "HTML", "CSS"]
        super().__init__(name, skills)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list[str] | None = None) -> None:
        if isinstance(skills, list):
            skills.extend(["Python", "SQL", "Django"])
        else:
            skills = ["Python", "SQL", "Django"]
        super().__init__(name, skills)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list[str] | None = None) -> None:
        if isinstance(skills, list):
            skills.extend(["Java", "Android studio"])
        else:
            skills = ["Java", "Android studio"]
        super().__init__(name, skills)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str, skills: list[str] | None = None) -> None:
        super().__init__(name, skills)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
