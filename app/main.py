class SoftwareEngineer:
    skills = []
    def __init__(self, name: str) -> None:
        self.name = name

    def learn_skill(self, skill: str) -> None:
        SoftwareEngineer.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str,
                 skills:
                 list=["JavaScript", "HTML", "CSS"]) -> None:
        super().__init__(name)
        self.skills = skills

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"