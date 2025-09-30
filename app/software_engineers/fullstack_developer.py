from app.software_engineers.backend_developer import BackendDeveloper
from app.software_engineers.frontend_developer import FrontendDeveloper
from app.software_engineers.software_engineer import SoftwareEngineer


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        SoftwareEngineer.__init__(self, name)
        self.skills += ["Python", "SQL", "Django", "JavaScript", "HTML", "CSS"]

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()