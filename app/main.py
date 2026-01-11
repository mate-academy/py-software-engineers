class SoftwareEngineer:
    skills = []

    def __init__(self, name: str) -> None:
        self.name = name

    def learn_skills(self, skill: str) -> None:
        self.skills.append(skill)
