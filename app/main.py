class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontDevMixin:
    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackDevMixin:
    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDevMixin:
    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FrontendDeveloper(SoftwareEngineer, FrontDevMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["JavaScript", "HTML", "CSS", ]


class BackendDeveloper(SoftwareEngineer, BackDevMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["Python", "SQL", "Django", ]


class AndroidDeveloper(SoftwareEngineer, AndroidDevMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["Java", "Android studio", ]


class FullStackDeveloper(FrontendDeveloper,
                         BackendDeveloper,
                         AndroidDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["Python", "SQL", "Django",
                       "JavaScript", "HTML", "CSS", ]

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        print(f"{self.name} is creating an API...")
        print(f"{self.name} is creating a webpage...")
        return
