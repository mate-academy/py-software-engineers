from typing import Optional


class SoftwareEngineer:
    def __init__(self,
                 name: str,
                 skills: Optional[list[str]] = None,
                 ) -> None:
        self.name = name
        self.skills = self.coords = skills if skills else []

    def learn_skill(self,
                    skill: str
                    ) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self,
                 name: str,
                 skills: Optional[list[str]] = None
                 ) -> None:
        super().__init__(name = name, skills = skills)
        if "JavaScript" not in self.skills:
            self.skills.append("JavaScript")
        if "HTML" not in self.skills:
            self.skills.append("HTML")
        if "CSS" not in self.skills:
            self.skills.append("CSS")

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self,
                 name: str,
                 skills: Optional[list[str]] = None
                 ) -> None:
        super().__init__(name = name, skills = skills)
        if "Python" not in self.skills:
            self.skills.append("Python")
        if "SQL" not in self.skills:
            self.skills.append("SQL")
        if "Django" not in self.skills:
            self.skills.append("Django")

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


def AndroidDeveloper(SoftwareEngineer):
    def __init__(self,
                 name: str,
                 skills: Optional[list[str]] = None
                 ) -> None:
        super().__init__(name = name, skills = skills)
        if "Java" not in self.skills:
            self.skills.append("Java")
        if "Android studio" not in self.skills:
            self.skills.append("Android studio")
