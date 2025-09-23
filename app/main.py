class SoftwareEngineer:
    def __init__(self, name: str, skills: list) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)
