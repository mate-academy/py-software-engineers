class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        front_skills = ["JavaScript", "HTML", "CSS"]
        self.skills.extend(front_skills)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        page = "<h1>Hello world</h1>"
        return page


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        back_skills = ["Python", "SQL", "Django"]
        self.skills.extend(back_skills)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        address = "http://127.0.0.1:8000"
        return address


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        andr_skills = ["Java", "Android studio"]
        self.skills.extend(andr_skills)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        app = "Ads every three swipes"
        return app


class FullStackDeveloper(
    FrontendDeveloper,
    BackendDeveloper
):
    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
