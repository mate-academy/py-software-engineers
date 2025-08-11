class SoftwareEngineer:
    def __init__(self, name: str):
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str):
        if skill not in self.skills:
            self.skills.append(skill)

    def __repr__(self):
        return f"{self.name} has skills: {', '.join(self.skills)}"


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.skills.extend(["JavaScript", "CSS", "HTML"])


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])


class FullStackDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        # Объединяем навыки Frontend и Backend
        self.skills.extend(["JavaScript", "CSS", "HTML", "Python", "SQL", "Django"])


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.skills.extend(["Java", "Android Studio"])