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