class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)

    def learn_many_skills(self, *skills_list) -> None:
        self.skills += list(skills_list)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.learn_many_skills("JavaScript", "HTML", "CSS")

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.learn_many_skills("Python", "SQL", "Django")

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.learn_many_skills("Java", "Android studio")

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
