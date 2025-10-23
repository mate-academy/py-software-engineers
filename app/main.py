class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills: list[str] = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FullStackDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Python", "JavaScript", "HTML", "CSS"])

    def create_powerful_tool(self) -> str:
        print(f"{self.name} is creating a powerful tool...")
        return "Tool created using an API."

    def create_awesome_web_app(self) -> str:
        print(f"{self.name} is creating a webapp...")
        return "Webapp created using Django."

    def create_awesome_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Mobile app created using React Native."
