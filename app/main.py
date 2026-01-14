class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.skills: list[str] = []

    def learn_skill(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)

    def __str__(self) -> str:
        return (f"Software Engineer: {self.name}, "
                f"Skills: {", ".join(self.skills) if self.skills else "None"}")


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills += ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills += ["Python", "SQL", "Django"]

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills += ["Java", "Android studio"]

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = list(dict.fromkeys(self.skills))

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        backend = self.create_powerful_api()
        frontend = self.create_awesome_web_page()
        return f"Frontend: {frontend}\nBackend: {backend}"
