class SoftwareEngineer:
    def __init__(self, name: str, skills: list | None = None) -> None:
        self.name = name
        if skills is None:
            self.skills = []
        else:
            self.skills = skills

    def learn_skill(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name, ["Javascript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world!</h1>"


engineer = SoftwareEngineer("Max")
# engineer.skills == []
engineer.learn_skill("Python")
print(engineer.skills)
