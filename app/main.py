class SoftwareEngineer:
    skills = []

    def __init__(self, name: str) -> None:
        self.name = name

    def learn_skills(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    skills = ["JavaScript", "HTML", "CSS"]

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"
