from app.developers.software_engineer import SoftwareEngineer


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend([
            "JavaScript",
            "HTML",
            "CSS",
        ])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"
