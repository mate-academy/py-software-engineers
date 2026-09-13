class SoftwareEngineer:
    def __init__(
        self, name: str, skills: list[str] | None = None,
        default_skills: list[str] | None = None
        ) -> None:
        self.name = name
        self.skills = skills if skills is not None else []
        for skill in default_skills:
            self.learn_skill(skill)
    
    def learn_skill(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(
        self, name: str, skills: list[str] | None = None
    ) -> None:
        default_skills = ["JavaScript", "HTML", "CSS"]
        super().__init__(name, skills)
        

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(
        self, name: str, skills: list[str] | None = None
    ) -> None:
        default_skills = ["Python", "SQL", "Django"] 
        super().__init__(name, skills)
        
    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(
        self, name: str, skills: list[str] | None = None
    ) -> None:
        default_skills = ["Java", "Android Studio"]
        super().__init__(name, skills)