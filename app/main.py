class SoftwareEngineer:
    def __init__(self, name: str, skills: list = None) -> None:
        self.name = name
        self.skills = skills if skills is not None else []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendEngineer(SoftwareEngineer):
    def create_web_page(self) -> str:
        return f"{self.name} is creating a web page..."


class BackendEngineer(SoftwareEngineer):
    def create_powerful_api(self) -> str:
        return f"{self.name} is creating a powerful API..."


class FullStackEngineer(FrontendEngineer, BackendEngineer):
    pass


class AndroidDeveloper(SoftwareEngineer):
    def create_smooth_mobile_app(self) -> str:
        return f"{self.name} is creating a smooth mobile app..."
