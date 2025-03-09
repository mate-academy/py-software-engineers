from typing import List

TSkills = List[str]


class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills: TSkills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)
