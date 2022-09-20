class SoftwareEngineer:
    skills = []

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def learn_skill(cls, skill: str):
        cls.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super(FrontendDeveloper, self).__init__(name=name)
        FrontendDeveloper.skills = [
            "JavaScript",
            "HTML",
            "CSS",
        ]

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super(BackendDeveloper, self).__init__(name=name)
        BackendDeveloper.skills = [
            "Python",
            "SQL",
            "Django",
        ]

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super(AndroidDeveloper, self).__init__(name=name)
        AndroidDeveloper.skills = [
            "Java",
            "Android studio",
        ]

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        super(FullStackDeveloper, self).__init__(name=name)
        FullStackDeveloper.skills = [
            "Python",
            "SQL",
            "Django",
            "JavaScript",
            "HTML",
            "CSS",
        ]

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
