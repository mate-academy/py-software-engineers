class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills: list[str] = []

    def learn_skill(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    DEFAULT_SKILLS = ("JavaScript", "CSS", "HTML")

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend([s for s in self.DEFAULT_SKILLS if s not in self.skills])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    DEFAULT_SKILLS = ("Python", "SQL", "Django")

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend([s for s in self.DEFAULT_SKILLS if s not in self.skills])

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    DEFAULT_SKILLS = ("Java", "Android studio")

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend([s for s in self.DEFAULT_SKILLS if s not in self.skills])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    DEFAULT_SKILLS = BackendDeveloper.DEFAULT_SKILLS + FrontendDeveloper.DEFAULT_SKILLS

    def __init__(self, name: str) -> None:
        SoftwareEngineer.__init__(self, name)
        self.skills.extend(self.DEFAULT_SKILLS)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
