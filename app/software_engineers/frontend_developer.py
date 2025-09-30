from app.software_engineers.software_engineer import SoftwareEngineer


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills += ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello World!</h1>"
