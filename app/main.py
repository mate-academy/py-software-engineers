class CreatingMixin:
    def creating(self, what_creating: str, what_return: str) -> str:
        print(f"{self.name} {what_creating}...")

        return what_return


class SoftwareEngineer:
    skills = []

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def learn_skill(cls, skill: str) -> None:
        cls.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer, CreatingMixin):
    skills = ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page(self) -> str:
        return self.creating("is creating a webpage",
                             "<h1>Hello world</h1>")


class BackendDeveloper(SoftwareEngineer, CreatingMixin):
    skills = ["Python", "SQL", "Django"]

    def create_powerful_api(self) -> str:
        return self.creating("is creating an API",
                             "http://127.0.0.1:8000")


class AndroidDeveloper(SoftwareEngineer, CreatingMixin):
    skills = ["Java", "Android studio"]

    def create_smooth_mobile_app(self) -> str:
        return self.creating("is creating a mobile app",
                             "Ads every three swipes")


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper, CreatingMixin):
    skills = ["JavaScript", "HTML", "CSS", "Python", "SQL", "Django"]

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")

        self.create_powerful_api()
        self.create_awesome_web_page()
