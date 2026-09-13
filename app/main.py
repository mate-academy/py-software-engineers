class SoftwareEngineer:
    def __init__(
        self, name: str, skills: list[str] | None = None
        ) -> None:
        self.name = name
        self.skills = skills if skills is not None else []
    
    def learn_skill(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(
        self, name: str, skills: list[str] | None = None
    ) -> None:
        super().__init__(name, skills)
        for skill in ["JavaScript", "HTML", "CSS"]:
            self.learn_skill(skill)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"
