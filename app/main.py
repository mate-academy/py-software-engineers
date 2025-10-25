class SoftwareEngineer():
    def __init__(self, name: str) -> None:

        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str,) -> None:
        skills = ["JavaScript", "HTML", "CSS"]
        super().__init__(name=name)
        self.skills.extend(skills)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        create_web = "<h1>Hello world</h1>"
        return create_web


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        skills = ["Python", "SQL", "Django"]
        super().__init__(name=name)
        self.skills.extend(skills)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        address_api = "http://127.0.0.1:8000"
        return address_api


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        skills = ["Java", "Android studio"]
        super().__init__(name=name)
        self.skills.extend(skills)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        ads = "Ads every three swipes"
        return ads


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str) -> None:
        skills = ["Python", "SQL", "Django", "JavaScript", "HTML", "CSS"]
        super().__init__(name=name)
        self.skills = skills

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
