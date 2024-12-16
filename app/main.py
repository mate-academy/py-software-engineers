from typing import List


class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.skills: List[str] = []

    def learn_skill(self, skill: str) -> None:
        # Приводим все навыки к нижнему регистру для согласованности
        self.skills.append(skill.lower())


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["javascript", "css", "html"]

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["python", "sql", "django"]


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["python", "sql", "django", "javascript", "css", "html"]

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        print(f"{self.name} is creating an API...")
        print(f"{self.name} is creating a webpage...")


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills = ["java", "android studio"]

    def learn_skill(self, skill: str) -> None:
        # Приводим все навыки к нижнему регистру
        super().learn_skill(skill)

    def print_skills(self):
        print(self.skills)